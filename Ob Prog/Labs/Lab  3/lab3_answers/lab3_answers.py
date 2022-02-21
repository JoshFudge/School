

#####################
# Q3

midterms = { "CP1520": [77, 83, 99], "CP1890": [57,79,82] }

# a
print(midterms['CP1890'][1]) # 79

# b
midterms['CR2800'] = [86, 77] 

# c
midterms['CR2800'].append(90)

# d
averages = {}
for course, grades in midterms.items():
    averages[course] = round(sum(grades)/len(grades))

print(averages)
#####################

#####################
# Q4

print("\n\n---Question 4---")

from random import randint

def dice_roll(n):
    dice_dictionary = {}
    for i in range(n):
        roll = randint(1, 6)
        if roll in dice_dictionary:
            dice_dictionary[roll] += 1
        else:
            dice_dictionary[roll] = 1
    return dice_dictionary

n = 10000
example_dictionary = dice_roll(n)

print(example_dictionary)

keys = list(example_dictionary)
keys.sort()

print(f"Rolling the dice {n} times:")
print()
for number in keys:
    print(f"Probability of rolling {number}: {round(example_dictionary[number] / n, 2)}")

