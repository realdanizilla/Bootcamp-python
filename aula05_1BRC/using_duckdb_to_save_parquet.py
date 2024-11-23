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

    result.show()

    # save to parquet file
    result.write_parquet('data/measurements_summary.parquet')

if __name__ == "__main__":
    create_duckdb()
