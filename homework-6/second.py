"""
2. დაწერეთ პროგრამა რომელიც წაიკითხავს data.txt ფაილს. ამ ფაილში მოცემულია
პროდუქციის შესყიდვის მონაცემები. მონაცემები ერთმანეთისგან გამოყოფილია მძიმით.
მონაცემების მიმდევრობა შემდეგია user_name,product_name,amount,price - სადაც price
არის ერთეული პროდუქციის ღირებულება. პროგრამამ უნდა გააკეთოს ორი ახალი
ფაილი small.txt და high.txt. პროგრამა small.txt ფაილში უნდა გადაწეროს ის შესყიდვები
რომელთა ღირებულება ნაკლებია 10-ზე, ხოლო ყველა სხვა დანარჩენი high.txt ფაილში.
"""

with open('files/data.txt', 'r') as data_file, open('files/high.txt', 'w') as high_file, open('files/small.txt', 'w') as small_file:
    for line in data_file:
        user_name, product_name, amount, price = line.split(',')
        str_to_write = f'{user_name},{product_name},{amount},{price}'
        total = float(price) * int(amount)
        if total < 10:
            small_file.write(str_to_write)
        else:
            high_file.write(str_to_write)
