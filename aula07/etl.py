# This relates to challenge on aula07
# Start by identifying functions needed (read_csv, filter_delivered_products, sum_product_prices, sum_categories)
# create function docstring to define what you need to do
# develop and test functions

import csv

def read_csv(file_name_csv: str) -> list[dict]:
    """This function reads a csv file and returns a list of dictionaries

    Args:
        file_name_csv (str): csv file name

    Returns:
        list[dict]: list of dictionaries with csv information
    """
    list = []
    with open(file_name_csv, mode="r", encoding="utf-8") as file: 
        reader = csv.DictReader(file)
        for row in reader:
            list.append(row)
    return list

# read_csv function test
# sales_items: list[dict] = read_csv(file_path)
# print(sales_items)

def filter_delivered_products(list:list[dict]) -> list[dict]:
    """This function filters products that have been delivered (delivered=True)

    Args:
        list (list[dict]): List of dictionaries containing products and their information

    Returns:
        list[dict]: List of dictionaries with products that were delivered
    """
    filtered_product_list = []
    for product in list:
        if product.get("delivered") == "True":
            filtered_product_list.append(product)
    return filtered_product_list

# filter_delivered_products function test (chained)
# product_list = read_csv(file_path)
# delivered_products = filter_delivered_products(product_list)
# print(delivered_products)

def sum_product_prices(list:list[dict]) -> int:
    """This function sums product prices

    Args:
        list (list[dict]): List of dictionaries containing products and their information

    Returns:
        int: sum of product prices
    """
    total = 0
    for product in list:
        total += int(product.get("price"))
    return total

# sum_product_prices function test (chained)
# product_list = read_csv(file_path)
# print(product_list)
# print()
# delivered_products = filter_delivered_products(product_list)
# print(delivered_products)
# print()
# total_prices = sum_product_prices(delivered_products)
# print(total_prices)

def sum_categories(list:list[dict]) -> list[dict]:
    """This functions multiplies quantity sold by price and creates a sum of per product category

    Args:
        list (list[dict]): List of dictionaries containing products and their information

    Returns:
        list[dict]: List of dictionaries with categories and total sales
    """
    category_dict = {}
    for product in list:
        category = product['category']
        price = float(product['price'])
        quantity = int(product['quantity'])
        total_value = price * quantity
    
        if category in category_dict:
            category_dict[category] += total_value
        else:
            category_dict[category] = total_value
    result = [{'category': category, 'total_value':total_value} for category, total_value in category_dict.items()]
    return result


# sum_categories function test (chained)
# product_list = read_csv(file_path)
# print(product_list)
# print()
# total_categories = sum_categories(product_list)
# print(total_categories)