import streamlit as st
import duckdb
import pandas as pd

# função para carregar dados do parquet
def load_data():
    con = duckdb.connect()
    df = con.execute("SELECT * from 'data/measurements_summary.parquet'").df()
    con.close()
    return df


# função do dashboard
def main():
    st.title("Weather station summary")
    st.write("This dashboard shows summary of weather stations")

    # carregar os dados
    data = load_data()

    # exibir como tabela
    st.dataframe(data)


if __name__ == "__main__":
    main()

