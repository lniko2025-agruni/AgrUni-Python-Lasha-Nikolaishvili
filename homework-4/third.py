"""
3. დაწერეთ ფუნქცია, რომელიც მიიღებს ორ ნატურალურ რიცხვს 10000-მდე და
ეკრანზე გამოიტანს მათ უმცირეს საერთო ჯერადს - LCM. იმპორტი გაუკეთეთ
საერთო გამყოფის ფუნქციას წინა მაგალითიდან და მისი საშუალებით
დაათვლევინეთ უმცირესი საერთო ჯერადი.
მინიშნება: lcm(a, b) = a * b / gcd(a, b).
მაგალითი 1:
Enter a: 1000
Enter b: 400
LCM of 1000 and 400 is 2000.
მაგალითი 2:
Enter a: 500
Enter b: 50
LCM of 500 and 50 is 500.
ფუნქციის ქვევით გამოიძახეთ ის რამდენიმეჯერ და დარწმუნდით მის
სისწორეში.
"""
from second import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

print('Test cases: ')
cases = [
    (13, 13, 13),
    (1, 9999, 9999),
    (270, 192, 270 * 192 // gcd(270, 192)),
    (10000, 5000, 10000),
    (17, 19, 17 * 19 // gcd(17, 19)),
    (12, 18, 12 * 18 // gcd(12, 18)),
]
for a, b, expected in cases:
    print(f'Is correct for {a}, {b}: ', lcm(a, b) == expected)

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(f'LCM of {a} and {b} is {lcm(a, b)}')