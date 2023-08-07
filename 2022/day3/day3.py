import os

file = open(os.path.join(os.getcwd(), "2022", "day3", "input.txt")).read().split('\n')
# for line in file : 
#     newLine = ''.join(sorted(line, key=lambda x: (x.swapcase(), x))) # ''.join is a manner to have directly a string not a table 
#     print(newLine[0:int(len(newLine)/2)]) 
#     print(newLine[int(len(newLine)/2):len(newLine)])
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