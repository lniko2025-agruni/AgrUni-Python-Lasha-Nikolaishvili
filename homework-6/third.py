"""
3. დაწერეთ პროგრამა რომელიც წინა ამოცანაში აღწერილი სტრუქტურის ფაილიდან
წაიკითხავს გაყიდვების ინფორმაციას.
a. პროგრამამ უნდა იპოვოს მაქსიმალური შესყიდვის (პროდუქტების რაოდენობით, ერთ
შესყიდვაში) განმხორციელებელი მომხმარებელი, თუ რამდენიმენა, მაშინ
მომხმარებლების სია.
b. პროგრამამ უნდა იპოვოს მაქსმალური შესყიდვის (ყველა შესყიდვის ჯამური
ღირებულებით) განმხორციელებელი მომხმარებელი, თუ რამდენიმენა, მაშინ
მომხმარებლების სია.
c. პროგრამამ უნდა იპოვოს შესყიდვების ღირებულების საშუალო არითმეტიკული.
d. პროგრამამ უნდა იპოვოს შესყიდვების რაოდენობების საშუალო არითმეტიკული.
e. პროგრამამ უნდა იპოვოს ყველაზე დიდი რაოდენობით გაყიდული პროდუქტი, თუ
რამდენიმეა მაშინ, პროდუქტების სია.
ნაპოვნი მონაცემები შეაგროვეთ dict ტიპის ობიექტში და ჩაწერეთ stats.json ფაილში.
დააფორმატეთ stats.json ფაილი ისე, რომ მონაცემები ჩაიწეროს ადვილად წაკითხვადი
ფორმით.
"""
import statistics
import json


sales = []
with open('files/data.txt', 'r') as data_file:
    for line in data_file:
        user_name, product_name, amount, price = line.split(',')
        customer = {
            "user_name": user_name, "product_name": product_name, "amount": int(amount), "price": float(price)
        }
        sales.append(customer)

# a
max_amount = max([s["amount"] for s in sales])
max_amount_sales = list(filter(lambda s: s["amount"] == max_amount, sales))
max_amount_persons = list(set(map(lambda s: s["user_name"], max_amount_sales)))

# b
total_values_obj = {}
for s in sales:
    if total_values_obj.get(s['user_name'], None):
        total_values_obj[s['user_name']] += s["amount"] * s["price"]
    else:
        total_values_obj[s['user_name']] = s["amount"] * s["price"]

max_value = max(total_values_obj.values())
max_value_persons = []
for k, v in total_values_obj.items():
    if v == max_value:
        max_value_persons.append(k)

# c
mean_value = round(statistics.mean([c["amount"] * c["price"] for c in sales]), 2)

# d
mean_amount = round(statistics.mean([c["amount"] for c in sales]), 2)

# e
total_amounts_obj = {}
for s in sales:
    if total_amounts_obj.get(s['product_name'], None):
        total_amounts_obj[s['product_name']] += s["amount"]
    else:
        total_amounts_obj[s['product_name']] = s["amount"]

max_amount = max(total_amounts_obj.values())
max_amount_products = []
for k, v in total_amounts_obj.items():
    if v == max_amount:
        max_amount_products.append(k)

stats_obj = {
    "person_stats": {
        "max_bought_by_amount": max_amount_persons,
        "max_bought_by_value": max_value_persons
    },
    "product_stats": {
        "max_bought_by_amount": max_amount_products
    },
    "general_sales_stats": {
        "mean_value": mean_value,
        "mean_amount": mean_amount
    }
}

with open('files/stats.json', 'w') as stats_file:
    json_stats_obj = json.dumps(stats_obj, indent=4)
    stats_file.write(json_stats_obj)