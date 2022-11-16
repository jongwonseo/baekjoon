A = input("")
nlist = A.split(" ")

def isSame(nlist):
    for i in range(len(nlist[0])):
        for j in range(len(nlist[1])):
            if nlist[0][i] == nlist[1][j]:
                return(True, i, j)
    return(False, 0, 0)

same, i, j = isSame(nlist)
if same == False:
    print("\nNone\n")
elif same == True:
    for x in range(len(nlist[1])):
        if x == i:
            print(nlist[1])
        else:
            print("."*j+nlist[0][x]+"."*(len(nlist[0])-j))