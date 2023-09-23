import os
file = open(os.path.join(os.getcwd(), "2022", "day5", "input.txt")).read().split('\n') # file est de type str 
copyfile = list(file)
col1 = ['Q','S','W','C','Z','V','F','T']
col2 = ['Q','R','B']
col3 = ['B','Z','T','Q','P','M','S']
col4 = ['D','V','F','R','Q','H']
col5 = ['J','G','L','D','B','S','T','P']
col6 = ['W','R','T','Z']
col7 = ['H','Q','M','N','S','F','R','J']
col8 = ['R','N','F','H','W']
col9 = ['J','Z','T','Q','P','R','B']

def numberToCol(nb) :
    if nb == 1 : 
        return col1
    elif nb == 2 :
        return col2 
    elif nb == 3 : 
        return col3 
    elif nb == 4 :
        return col4
    elif nb == 5 : 
        return col5 
    elif nb == 6 :
        return col6
    elif nb == 7 : 
        return col7
    elif nb == 8 :
        return col8 
    elif nb == 9 : 
        return col9
    else : # cas d'erreur 
        return 0  


# Variable col commune donc obligé de mettre une partie en commentaire 

# PART 1 
    
# file.reverse()
# while(len(file)>0) : 
#     line = file.pop().replace(" ","")
#     if "move" in line : 
#         line = line.replace("move","").replace("from",",").replace("to",",").split(',')
#         nbLettre = line[0]
#         oldCol = numberToCol(int(line[1]))
#         newCol = numberToCol(int(line[2]))
#         for _ in range(int(nbLettre)) :
#             newCol.append(oldCol.pop()) 
# answer = ""
# for _ in range(1,10) : # de 1 jusqu'à 10 
#     num = numberToCol(_)
#     answer = answer + num.pop()
# print(answer)
# Du 1er coup :)

# PART 2 
copyfile.reverse()
while(len(copyfile)>0) :
    line = copyfile.pop().replace(" ", "")
    if "move" in line : 
        line = line.replace("move","").replace("from",",").replace("to",",").split(',')
        nbLettre = line[0]
        oldCol = numberToCol(int(line[1]))
        newCol = numberToCol(int(line[2]))
        tempCol = list() # autre manière d'initialiser une liste que de faire tempCol = []
        for _ in range(int(nbLettre)) :
            tempCol.append(oldCol.pop())
        tempCol.reverse()
        newCol.extend(tempCol) # auparavant je faisais newCol = newCol + tempCol ce qui créer des pb de référencement
answer=""
for _ in range(1,10) : # de 1 jusqu'à 10 
    num = numberToCol(_)
    if len(num) >0 : 
        answer = answer + num.pop()
print(answer)


