import os
# PART 1 
file = open(os.path.join(os.getcwd(), "2022", "day4", "input.txt")).read().split('\n')
newList = [segment for element in file for segment in element.replace(',', '-').split('-')]
# La ligne du dessus se traduit de manière plus classique en :
# for i in file : 
#     list = i.replace(',', '-').split('-')
#     print(list)
#     for h in list : 
#         print(h)
print(newList)
cpt = 0
while(len(newList)>0) : 
    pos4 = int(newList.pop())
    pos3 = int(newList.pop())
    pos2 = int(newList.pop())
    pos1 = int(newList.pop())
    if pos1 - pos3 <= 0 and pos2-pos4 >=0 or pos1-pos3>=0 and pos2-pos4<=0 :
        cpt=cpt+1
print(cpt)
    