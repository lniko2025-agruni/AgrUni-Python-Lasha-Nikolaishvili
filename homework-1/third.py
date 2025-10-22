n = input("Enter a number less than or equal to 100: ")

while not n.isdigit() or int(n) > 100:
    n = input("Invalid input. Please enter a number less than or equal to 100: ")

n = int(n)

def fibonacci(num):
    a, b = 0, 1
    sequence = []
    for _ in range(num):
        sequence.append(a)
        a, b = b, a + b
    return sequence

fib_sequence = fibonacci(n)
print("Fibonacci sequence members:", fib_sequence)
