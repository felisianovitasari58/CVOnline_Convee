map=[True,True,True,False,True,True,True,True],[True,True,False,False,False,True,True,False],[True,True,True,True,True,True,True,False],[True,True,True,True,True,True,True,False],[False,False,False,True,True,True,True,False],[True,True,True,False,False,True,True,False],[True,True,True,True,True,True,False,True],[True,True,True,True,False,False,True,True]
# start=[0][1]
# stop=[6][4]

# urut=False
# while not urut:
#     urut= True
#     for i in range(len(nilai)-1):
#         if(nilai[i]>nilai[i+1]):
#             min=nilai[i+1]
#             nilai[i+1]=nilai[i]
#             nilai[i]=min
#             urut=False
#
#     print(nilai)

temp=[]
temp1=[]
x=0
y=0
i=0
j=1
while  (x<=6) :
# for i in range(len(map)):
#     for j in range(1,len(map)):
    if(map[i][j]==True):
        temp.append(i)
        x=i
        temp1.append(j)
        y=j
        j+=1
        # if(map[i][j]==False):
        #     x=i
        #     y=j
        #     j-=1
    elif(map[i][j]==False):
        j-=1
        i+=1
        x=i
        y=j

print(temp)
print(temp1)
# coba edit
######


