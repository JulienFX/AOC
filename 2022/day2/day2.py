import os
'PART 1' 
lines = open(os.path.join(os.getcwd(), "2022", "day2", "input.txt")).read().split('\n')
res = 0
for line in lines:
    opp=ord(line[0]) - ord('A')
    me=ord(line[2]) - ord('X')
    res += 1 + me + 3 * ((1 + me - opp) % 3) # tricky formula, do some example to uderstand it 

# print(res)
# ord() refers to the ascii table 

'PART 2 '
result = 0 
for line in lines: 
    opp=ord(line[0]) - ord('A')
    if(line[2]=='X') :
        me=(opp + 2) % 3
    elif(line[2]=='Y') :
        me=opp
    else : 
        me = (opp + 1) % 3
    result += 1 + me + 3 * ((1 + me - opp) % 3)  
print(result)
