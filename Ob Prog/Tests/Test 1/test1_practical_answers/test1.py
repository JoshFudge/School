# Q1 Write a function that uses the math module to calculate the area of a circle. Return a result that is rounded to 2-digits. Test your function three times using radius values of 1, 2, and 3.

print()
print("--Question 1--")

import math

def area_of_circle(r):
    return round(math.pi * math.pow(r, 2), 2)

print(area_of_circle(1))
print(area_of_circle(2))
print(area_of_circle(3))

print()

# Q2 Output the following data in the format shown in the output below using f-string formatting.

print()
print("--Question 2--")

contacts = {
    "Bob": ["bob@bestbobs.com", "709-555-5555"],
    "Alice": ["alice@blizzard.com", "709-555-5556"]
}

print(f"{'Name':20} {'Email':>20} {'Phone':>20}")

for key, value in contacts.items():
    print(f"{key:20} {value[0]:>20} {value[1]:>20}")


print()

# Q3 Given the following string named full_path, use the split and join string methods to arrive at the output shown below

### output: home --> joel --> Documents --> songs --> futuredays.md

print()
print("--Question 3--")

full_path = "/home/joel/Documents/songs/future_days.md"

path_list = full_path.split("/")
path_list.remove("")

print(" --> ".join(path_list))


print()

# Q4

print()
print("--Question 4--")

grades = {
    "John": 89,
    "Tim": 75,
    "Molly": 100,
    "Roger": 81
}

grades["Alice"] = 66
print(grades)
print(grades["Molly"])
print(sum(list(grades.values()))/len(grades))

#


print()

# Q5 Create a dictionary where the keys are the characters of your first name and the values are the ordinal encodings of that character. Then, recreate your name as a string using the values of the dictionary. (use the ord and chr built-ins to answer this question)

print()
print("--Question 5--")

name = "John"
name_encoding = {}
for c in name:
    name_encoding[c] = ord(c)

print(name_encoding)

for encoding in name_encoding.values():
    print(chr(encoding), end="")

