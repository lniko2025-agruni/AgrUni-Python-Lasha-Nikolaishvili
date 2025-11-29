"""
1. დაწერეთ ფუნქცია, რომელიც დაადგენს გადაცემული რიცხვი მარტივია თუ არა
და დააბრუნებს True-ს მარტივის შემთხვევაში და False-ს შედგენილის
შემთხვევაში. ფუნქციის ქვევით გამოიძახეთ ის რამდენიმე რიცხვისთვის და
დაბეჭდეთ შედეგი.
"""
import math


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

print(f"-3 is prime", is_prime(-3))
print(f"0 is prime", is_prime(0))
print(f"1 is prime", is_prime(1))
print(f"2 is prime", is_prime(2))
print(f"3 is prime", is_prime(3))
print(f"4 is prime", is_prime(4))
print(f"5 is prime", is_prime(5))
print(f"12 is prime", is_prime(12))
print(f"13 is prime", is_prime(13))
print(f"97 is prime", is_prime(97))