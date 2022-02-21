import random

print("Probability calculator")
print()
n = int(input("Enter amount of time: "))
def roll(n):
    die_rolls = {}
    for i in range(1,n):
        
        roll = random.randint(1,6)
        if roll in die_rolls:
            die_rolls[roll]+=1
        else:
            die_rolls[roll]=1
    return die_rolls

example = roll(n)
print(example)

keys = list(example)
keys.sort()

for number in keys:
    print(f"Probability of rolling {number}:   {round(example[number]/n,2)}  ")