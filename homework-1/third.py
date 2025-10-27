n = input("Enter a number less than or equal to 100: ")

while not n.isdigit() or int(n) > 100:
    n = input("Invalid input. Please enter a number less than or equal to 100: ")

n = int(n)

def fibonacci(num):
    if num == 0 or num == 1:
        return num

    sequence = [0, 1]
    for _ in range(2, num):
        sequence.append(sequence[-2] + sequence[-1])
    return sequence

fib_sequence = fibonacci(n)
print("Fibonacci sequence members:", fib_sequence)
