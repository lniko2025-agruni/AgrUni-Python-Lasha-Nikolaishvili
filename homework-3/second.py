"""
დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს. პროგრამამ უნდა შეამოწმოს
არის თუ არა შესაძლებელი ერთი სტრიქონის სიმბოლოების გამოყენებით მეორე
სტრიქონის მიღება. შემოწმება უნდა იყოს case insensitive.
მაგალითი 1.
Input:
Listen
silent
Output: YES
მაგალითი 2.
Input:
a gentleman
Elegant man
Output: YES
მაგალითი 3.
Input:
dormitory
dirty room
Output: NO
მაგალითი 4.
Input:
election
collection
Output: NO
"""

str1 = input("Enter first string:").lower()
str2 = input("Enter second string:").lower()

def count_chars(string):
    counter = dict()
    for c in string:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    return counter

if count_chars(str1) == count_chars(str2):
    print('Yes')
else:
    print('No')