"""
დაწერეთ პროგრამა რომელიც დააგენერირებს 5 ცალ შემთხვევით რიცხვს 1-დან 4-მდე
და ჩაწერს სიაში. პროგრამამ უნდა გადაუაროს სიას და თითოეული ელემენტისთვის ეს
ელემენტი ჩაწეროს ახალ სიაში, იმდენჯერ, რაც არის მისი მნიშვნელობა. დაბეჭდეთ
ახალი სიის სიგრძე და თვითონ სია ეკრანზე.
მაგალითი: ვთქვათ პროგრამამ დააგენერირა სია, [1, 4, 2, 2, 3].
უნდა დაიბეჭდოს
List - [1, 4, 4, 4, 4, 2, 2, 2, 2, 3, 3, 3]
Length - 12
"""
from random import randint

nums = []
for i in range(5):
    nums.append(randint(1, 4))

occurrences_list =  []
for num in nums:
    occurrences_list += [num] * num

print(f"nums list - {nums}") # For reference
print(f"List - {occurrences_list}")
print(f"Length - {len(occurrences_list)}")
