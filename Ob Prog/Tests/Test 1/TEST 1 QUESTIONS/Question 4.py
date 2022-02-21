grades = {
    "John": 89,
    "Tim": 75,
    "Molly": 100,
    "Roger": 81
}
grades["Alice"] = 66
print(grades)
print(grades["Molly"])


total = 0
for grade in grades.values():
    total = total + grade

average = total/ len(grades)
print(average)
