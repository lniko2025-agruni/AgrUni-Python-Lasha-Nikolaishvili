"""
2. დაწერეთ ფუნქცია, რომელიც მიიღებს ორ ნატურალურ რიცხვს 10000-მდე და
ეკრანზე გამოიტანს მათ უდიდეს საერთო გამყოფს - GCD.
მაგალითი 1:
Enter a: 1000
Enter b: 400
GCD of 1000 and 400 is 200.
მაგალითი 2:
Enter a: 10000
Enter b: 17
GCD of 10000 and 17 is 1.
ფუნქციის ქვევით გამოიძახეთ ის რამდენიმეჯერ და დარწმუნდით მის
სისწორეში.
"""

def gcd(a, b):
    ret = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ret = i

    return ret

if __name__ == '__main__':
    print('Test cases: ')
    cases = [
        (13, 13, 13),
        (1, 9999, 1),
        (270, 192, 6),
        (10000, 5000, 5000),
        (17, 19, 1),
        (12, 18, 6),
    ]
    for a, b, expected in cases:
        print(f'Is correct for {a}, {b}: ', gcd(a, b) == expected)


    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print(f'GCD pf {a} and {b} is', gcd(a, b))
