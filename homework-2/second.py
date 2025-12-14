"""
მოცემულია სტუდენტების ქულები ფიზიკაში, მათემატიკაში და ქიმიაში.
subjects = {
'math': {'George': 85, 'Salome': 78, 'David': 92},
'physics': {'George': 90, 'David': 75, 'Salome': 88},
'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}
შექმენით და ეკრანზე გამოატანინეთ ლექსიკონი რომლის გასაღებებიც იქნება
სტუდენტის სახელები, ხოლო მნიშვნელობები ექნება ასევე ლექსიკონები, რომელთა
გასაღებები იქნება საგნის სახელები, და მნიშვნელობები - შესაბამისი ქულები.
Output: {'George': {'math': 85, 'physics': 90, 'chemistry': 80}, ...}
"""
from collections import defaultdict

subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

students = defaultdict(dict)

for subject, grades in subjects.items():
    for name, grade in grades.items():
        students[name].update({subject: grade})

print(f"Output: {dict(students)}")

