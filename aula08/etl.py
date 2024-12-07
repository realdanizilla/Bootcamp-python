# funções a criar:
# ler um arquivo e concatenar arquivos
# transformar arquivos calculando total venda (venda * qtde)
# load dos arquivos (decidir por dois caminhos csv ou parquet)

# arquivo etl.py vai ter as funções
# arquivo pipeline.py vai invocar - roda no airflow
# arquivo schema - de qualidade, schema / validação do dataframe
# pasta dados para arquivo json - json é o dicionário do javascript

import pandas as pd
import os
import glob


def extract_and_consolidate_data(pasta:str) -> pd.DataFrame:
    """This function extracts data from json files on a folder and concatenates them into a single dataframe

    Args:
        pasta (str): folder where json files are stored

    Returns:
        pd.DataFrame: dataframe with information from all json files on the folder
    """
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    # print(arquivos_json)
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    # print(df_list)
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def calculate_sales_total(df:pd.DataFrame) -> pd.DataFrame:
    """This function creates a new column in the dataframe with the calculation of total sales, which is a multiplication of 'quantidade' and 'venda' fields

    Args:
        df (pd.DataFrame): dataframe with 'quantidade' and 'venda' columns

    Returns:
        pd.DataFrame: dataframe with added column 'total'
    """
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

def load_data(df:pd.DataFrame, output_format:list):
    """This function generates csv and/or parquet files based on a dataframe

    Args:
        df (pd.DataFrame): the dataframe to be converted into one of the expected formats
        output_format (list): the expected output format 'csv', 'parquet' or both
    """
    for format in output_format:
        if format == 'csv':
            df.to_csv("data/data.csv", index=False)
        if format == 'parquet':
            df.to_parquet("data/data.parquet", index=False)

def pipeline_calculate_sales_total(pasta:str, output_format:list):
    """This function runs the entire pipeline of extraction, consolidation, transformation and loading

    Args:
        pasta (str): folder where json files are stored
        output_format (list): expected file format to be generated 'csv', 'parquet' or both
    """
    data_frame = (extract_and_consolidate_data(pasta))
    new_df = calculate_sales_total(data_frame)
    load_data(new_df, output_format)


if __name__ == '__main__':
    pasta_argumento: str = 'data'
    data_frame = (extract_and_consolidate_data(pasta=pasta_argumento))
    new_df = calculate_sales_total(data_frame)
    format: list = ['csv', 'parquet']
    loaded_data = load_data(new_df, format)
    print(loaded_data)