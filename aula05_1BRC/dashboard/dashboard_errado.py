import streamlit as st
import duckdb
import pandas as pd



def create_duckdb():
    result = duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station
    """)

# convertendo para df
    df = result.df()
    return df

# função do dashboard
def main():
    st.title("Weather station summary")
    st.write("This dashboard shows summary of weather stations")

    # carregar os dados
    data = create_duckdb()

    # exibir como tabela
    st.dataframe(data)


if __name__ == "__main__":
    main()


