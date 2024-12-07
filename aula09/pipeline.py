from etl import pipeline_calculate_sales_total

pasta: str = 'data'
format: list = ['csv', 'parquet']

pipeline_calculate_sales_total(pasta,format)
