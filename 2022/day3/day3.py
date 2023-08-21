import os
from collections import Counter
file = open(os.path.join(os.getcwd(), "2022", "day3", "input.txt")).read().split('\n')
# PART 1
sum = 0 
for line in file : 
    # set() => string to list 
    firstCompartment = set(line[:int(len(line)/2)]) # no need to precise before : 
    secondCompartment = set(line[len(line)//2:]) # no need to precise after : and with // the result will be automaticly an integer 
    common = (firstCompartment.intersection(secondCompartment)).pop() # intersection => find common char, pop return the common char with the good format which means not inside a table  
    if common.isupper():
        sum += ord(common) - ord('A') + 27
    else:
        sum += ord(common) - ord('a') + 1
print(sum)
# PART 2 
rucksack_sum = 0
while len(file) > 0:
    # take out first 3 entries
    first_rucksack = set(file.pop()) # by default will return the last elem of the file 
    second_rucksack = set(file.pop())
    third_rucksack = set(file.pop())
    # NOW we've got the 3 last lines of our file 
    overlap_char = ((first_rucksack.intersection(second_rucksack)).intersection(third_rucksack)).pop()

    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1
print(rucksack_sum)
