import os

lines = open(os.path.join(os.getcwd(), "2022", "day2", "input.txt")).read().split('\n')
res = 0
for line in lines:
    opp=ord(line[0]) - ord('A')
    me=ord(line[2]) - ord('X')
    res += 1 + me + 3 * ((1 + me - opp) % 3) # tricky formula, do some example to uderstand it 

print(res)
# ord() refers to the ascii table 
