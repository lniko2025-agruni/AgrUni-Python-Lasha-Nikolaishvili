from pprint import pprint


employees = [
    {"name": "Alice", "tasks": [5, 7, 9], "department": "IT"},
    {"name": "Bob", "tasks": [2, 3, 4], "department": "Sales"},
    {"name": "Charlie", "tasks": [8, 7, 6], "department": "IT"},
    {"name": "Diana", "tasks": [9, 8, 10], "department": "Marketing"},
    {"name": "George", "tasks": [2, 7, 6], "department": "IT"}
]

# 1
employees2 = list(map(
    lambda employee: {
        "name": employee["name"],
        "department": employee["department"],
        "average_tasks": sum(employee["tasks"])/len(employee["tasks"])
    },
    employees
))

print("Employee average tasks:")
pprint(employees2)

# 2
employees3 = sorted(employees2, key=lambda employee: employee["average_tasks"], reverse=True)
print("Employees by most average tasks completed:")
pprint(employees3)

# 3
best_employee = max(employees2, key=lambda employee: employee["average_tasks"])
print("Employee with most completed tasks")
print(best_employee)

# 4
best_it_employees = list(filter(
    lambda employee: employee["average_tasks"] > 6 and employee["department"] == "IT", employees2
))
print("Best performing it employees")
print(best_it_employees)