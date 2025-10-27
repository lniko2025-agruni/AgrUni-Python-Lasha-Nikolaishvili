n = int(input("Enter a number: "))

while not (1 <= n <= 1000):
    n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    if n % i == 0:
        print((int(n / i)), end=' ')
    