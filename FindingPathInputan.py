map=[True,True,True,False,True,True,True,True],[True,True,False,False,False,True,True,False],[True,True,True,True,True,True,True,False],[True,True,True,True,True,True,True,False],[False,False,False,True,True,True,True,False],[True,True,True,False,False,True,True,False],[True,True,True,True,True,True,False,True],[True,True,True,True,False,False,True,True]

temp=[]
temp1=[]
a=0
b=0
xStart=int(input("Titik start X= "))
yStart=int(input("Titik start Y= "))
xFinish=int(input("Titik stop X= "))
yFinish=int(input("Titik stop Y= "))
i=xStart
j=yStart
def finished(x,y):
    if(x==xFinish and y==yFinish):
        return True
    else:
        return False

while  (finished(a,b)==False) :
    if(map[i+1][j]==True):
        temp.append(i)
        a=i
        temp1.append(j)
        b=j
        i+=1
    elif(map[i+1][j]==False):
        if(map[i][j+1]==True):
            temp.append(i)
            a = i
            temp1.append(j)
            b = j
            j += 1
        elif(map[i][j+1]==False):
            a=i
            b=j
            temp.append(i)
            a = i
            temp1.append(j)
            b = j
            j-=1

print("Path untuk start dari ",xStart,",",yStart,"ke ",xFinish,",",yFinish, "ialah : ")
print("[",end="")
for m in range(len(temp)):
    print("(",temp[m],",",temp1[m],")",end="")
print("]")
# print(temp)
# print(temp1)
# coba edit
######

