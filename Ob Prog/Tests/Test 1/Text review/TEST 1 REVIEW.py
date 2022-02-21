# #################################################################################################CHAPTER 9
# from decimal import ROUND_HALF_UP, Decimal
# import locale as lc

# lc.setlocale(lc.LC_ALL, "en_CA") # en_US, en_UK, de_DE, ru_RU

# switch_oled = 449.99
# hst_rate = 0.15
# total = lc.currency(switch_oled * (1 + hst_rate))
# print(total)

# table = ['Sjoerd','Jack','Dcab'] 
# for name in table: 

#     print(f'{name:10}') 
 
# print() 
# table2 = [4127, 4098,  7678] 
# for num in table2: 
#     print(f'{num:10}')

# print()
# number = 1000000
# print(f'The number, 1000000, formatted with a comma {number:,.2f}') 
# print(f'The number, 1000000, formatted with a comma and right-aligned in a width of 15 {number:>15,.2f}')
# print()
# value = Decimal("15.105")
# value = value.quantize(Decimal("1.00"), ROUND_HALF_UP)
# print(value)

#################################################################################################CHAPTER 10

# name = "I first battled the Metroids on planet Zebes."

# print(name[0:7])

# print(name[0::2])

# print("work, " * 5, "work")
# print("He said me haffi ", "work, " * 5, "work")

#################################################################################################CHAPTER 12


# game = {
#     "name": "Warcraft II: Tides of Darkness",
#     "developer": "Blizzard Entertainment Inc.",
#     "year_released": 1995,
#     "game_type": "Real-time strategy",
#     "platforms": ["DOS", "Macintosh"],
#     "box_art": "https://www.mobygames.com/images/covers/l/6460-warcraft-ii-tides-of-darkness-dos-front-cover.jpg"
# }

# # access the VALUE by using the KEY
# print(f"\n{game['name']}")

# contacts = {
#     "Bob": "124-1242", 
#     "Alice": "325-5353"
# }

# for name in contacts.keys():
#     print(name)

# for num in contacts.values():
#     print(num)

# for name, num in contacts.items():
#     print(f"{name:10} {num}")




# x = input("Enter a sentence:    ").lower()

# alphabet=('abcdefghijklmnopqrstuvwxyz')
# lettercount={}

# for c in x:
#     if c in alphabet:
#         if c in lettercount:
#             lettercount[c] = lettercount[c] + 1
#         else:
#             lettercount[c] = 1

# print(lettercount)



# lettercount = list(lettercount.items())

# print(lettercount)

# for letter in lettercount:
#     print(f"{letter[0]:<45} {letter[1]}")



# def translator():
#     pwords = {}
#     pwords['hello'] = "haa'rr"
#     pwords['friends']= "mateys"

#     psentence = []
#     sentence = input("Enter a sentence: ")
#     words = sentence.split()


#     for word in words:
#         if word in pwords:
#             psentence.append(pwords[word])
#         else:
#             psentence.append(word)


#     return " ".join(psentence)



# h = translator()
# print(h)





# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }

# inventory['pocket']= ['seashell', 'strange berry','lint']
# inventory['backpack'].sort()


# inventory['backpack'].remove('dagger')
# inventory['gold'] = inventory['gold']+ 50
# print(inventory)



# prices = {
# "banana": 4,
# "apple": 2,
# "orange": 1.5,
# "pear": 3
# }

# stocks = {
# "banana": 5,
# "apple": 20,
# "orange": 100,
# "pear": 35


# }

# for food in prices:
#     print(food)
#     print(f"{prices[food]}")
#     print(f"{stocks[food]}")

# total = 0

# for food in prices:
#    food_cost = prices[food] * stocks[food]
#    total += food_cost
# print(total)




inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory["pocket"] = 'seashell', 'strange berry','lint'

inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold' ]+50


print(inventory)

prices = {}
prices["banana"] = 4
prices ["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3

stocks={}
stocks["apple"]= 10
stocks["banana"]=2
stocks["orange"] = 3
stocks["pear"] = 0

for food in prices:
    print(f"{food}")
    print(f"price:{prices[food]}")
    print(f"stock:{stocks[food]}")
    print()

total = 0
for food in prices.keys():
    sum = prices[food] * stocks[food]
    total += sum
print(total)


shopping_list ={"banana","orange","apple"}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total=0
    for food in food:
        if stock[food]> 0:
            total+= prices[food]
            stock[food]=stock[food]-1
    return total

answer = compute_bill(shopping_list)
print(answer)



# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0,97.0,75.0,92.0],
#   "quizzes": [88.0,40.0,94.0],
#   "tests": [75.0,90.0]
# }
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }
# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }


# students=[tyler,alice,lloyd]
# for student in students:
#     print(student["name"])
#     print(student["homework"])
#     print(student["quizzes"])
#     print(student["tests"])
#     print()

# def average(numbers):
#     total = float(sum(numbers))
#     total= total/(len(numbers))
#     return total

# def get_average(student):
#     student_hw = average(student["homework"])
#     student_qz = average(student["quizzes"])
#     student_ts = average(student["tests"])

#     student_hw = student_hw * 0.1
#     student_qz = student_qz * 0.3
#     student_ts = student_ts * 0.6
#     sum = (student_ts+ student_qz + student_hw)
#     return sum


# def get_letter_grade(score):
#     if score >= 80:
#         return "A"
#     elif score >= 70 and score <80:
#         return "B"
#     elif score >= 60 and score <70:
#         return "c"
#     else:
#         return "F"

# print (get_letter_grade(get_average(tyler)))

# def get_class_average(students=[lloyd,alice,tyler]):
#     results = []
#     for student in students:
#        result =get_average(student)
#        results.append(result)
#        return results

# print (get_class_average(students))
# print(get_letter_grade(get_class_average(students)))


x = input("Enter a sentence")
x = x.lower()

alphabet =("abcdefghijklmnopqrstuvwxyz")
letters={}
for char in x:
    
    if char in alphabet:
        if char in letters:
            letters[char]+= 1
        else:
            letters[char] = 1
keys = letters.keys()
for char in sorted(keys):
    print(char,letters[char])