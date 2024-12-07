from etl import read_csv, filter_delivered_products, sum_product_prices, sum_categories

file_path = "sales.csv"

product_list = read_csv(file_path)
print(product_list)
print()

delivered_products = filter_delivered_products(product_list)
print(delivered_products)
print()

total_prices = sum_product_prices(delivered_products)
print("total: ", total_prices)
print()

total_categories = sum_categories(product_list)
print(total_categories)