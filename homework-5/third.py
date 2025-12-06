import functools

products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]

# 1
available_products = list(filter(lambda product: product[2], products))
print("Available products:", available_products)

# 2
calculated_values = list(map(lambda product:(product[0], product[1] * product[2]), products))
print("Calculated values:", calculated_values)

# 3
total_value = functools.reduce(lambda total, product: total + product[1] * product[2], available_products, 0)
print("Total value:", total_value)