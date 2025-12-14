"""
პროგრამამ უნდა შეგვაყვანინოს წელიწადი და დაგვიბეჭდოს ნაკიანია თუ არა.
წელიწადი ნაკიანია თუ 400-ზე იყოფა, ან 4-ზე იყოფა მაგრამ 100-ზე არა. პროგრამამ
უნდა მოგთხოვოთ სწორი რიცხვის შეყვანა. მაგალითად, არანატურალური რიცხვის, ან
ციფრების გარდა სხვა სიმბოლოების შეყვანის შემთხვევაში თავიდან უნდა
მოგვთხოვოს რიცხვის შეყვანა.
"""
year = input("Enter a year: ")

while not year.isdigit() or int(year) < 0:
    year = input("Please enter a valid positive year: ")

year = int(year)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} isn't a leap year.")