# Python 3.9.15 virtual anaconda environnement 
'PART 1' 
import os 
print (max(sum(int(value) for value in group.split('\n') if value.strip()) for group in open(os.getcwd()+"\\2022\\day1\\input.txt").read().split('\n\n')))
# read() => read the content of the file in a single string
# split() => separator - \n return line \n\n return line x2 which means empty line
# list comprehension : https://python.doctor/page-comprehension-list-listes-python-cours-debutants : DO THIS / FOR THIS / "IN THAT SITUATION" 

# # Avec indentation
# input_file = os.getcwd() + "\\2022\\day1\\input.txt"
# with open(input_file, 'r') as file:
#     data = file.read()

# groups = data.split('\n\n')

# max_calories = 0
# for group in groups:
#     calories = [int(value) for value in group.split('\n') if value.strip()]
#     group_calories = sum(calories)
#     max_calories = max(max_calories, group_calories)

'PART 2'
calories = [sum(map(int, filter(None, group.split('\n')))) for group in open(os.getcwd()+"\\2022\\day1\\input.txt").read().split('\n\n')]
top_three_calories = sum(sorted(calories, reverse=True)[:3])
print(top_three_calories)

