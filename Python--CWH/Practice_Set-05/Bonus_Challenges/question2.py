# Given a dictionary of products and their prices, find the product with the highest price.

def find_most_expensive_product(products):
    if not products:
        return None, None
    most_expensive_product = max(products, key=products.get)
    return most_expensive_product, products[most_expensive_product]

products = {"Product A": 10, "Product B": 20, "Product C": 15}
most_expensive_product, price = find_most_expensive_product(products)
print(f"The most expensive product is {most_expensive_product} with a price of {price}")
    