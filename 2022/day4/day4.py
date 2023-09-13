import os
# PART 1 
file = open(os.path.join(os.getcwd(), "2022", "day4", "input.txt")).read().split('\n')
newList = [segment for element in file for segment in element.replace(',', '-').split('-')]
newList2 = list(newList) # création d'une copie 
# La ligne du dessus se traduit de manière plus classique en :
# for i in file : 
#     list = i.replace(',', '-').split('-')
#     print(list)
#     for h in list : 
#         print(h)
# print(newList)

cpt = 0
while(len(newList)>0) : 
    pos4 = int(newList.pop())
    pos3 = int(newList.pop())
    pos2 = int(newList.pop())
    pos1 = int(newList.pop())
    if pos1 - pos3 <= 0 and pos2-pos4 >=0 or pos1-pos3>=0 and pos2-pos4<=0 :
        cpt=cpt+1
print(cpt)
# PART 2 
cp = 0
while(len(newList2)>0) : 
    pos4 = int(newList2.pop())
    pos3 = int(newList2.pop())
    list2 = set(list(range(pos3,pos4+1))) #le +1 est nécessaire car range(n,p) renvoie rien si n=p  
    pos2 = int(newList2.pop())
    pos1 = int(newList2.pop())
    list1 = set(list(range(pos1,pos2+1)))
    overlap_int = list1.intersection(list2)
    if len(overlap_int)>0 :
        cp=cp+1
print(cp)