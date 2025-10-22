a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

while a + b <= c or a + c <= b or b + c <= a:
    print("Invalid input, try again.")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

triangle_perimeter = a + b + c
print("The perimeter of the triangle is:", triangle_perimeter)
semi_perimeter = triangle_perimeter / 2
area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

print("The area of the triangle is:", area)