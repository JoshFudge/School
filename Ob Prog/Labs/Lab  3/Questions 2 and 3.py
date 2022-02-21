#Question 2
print('Question 2\n')
instructors = {
    'CP3415' : 'Vasantha Adluhri',
    'CP1935' : 'Shivaji Patil',
    'CP1890' : 'John Milley'
}

games = {
    "title": "Marvels Spider-Man",
    "year_released": 2018,
    "platforms": ["PS4", "PS5"]
}
print(f"{games['title']}")
print(f"{games['platforms']}")
print(f"{games['year_released']}")
print()
print()


#Question 3
midterms = { "CP1520": [77, 83, 99], "CP1890": [57,79,82] }
print('Question 3\n')
print(midterms["CP1890"][1])

midterms['CR2800'] = [86,77]
midterms["CR2800"].append(90)
print(midterms["CR2800"])
print()

for courses, grades in midterms.items():

    average = (sum(grades) / len(grades))
    average = round(average)
   
    averages = {courses : average}
    print(averages)