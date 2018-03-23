minuman=["kopi","capuccino","frappucino"],["jus apel","jus jeruk","jus alpukat"]
print(minuman[1][1])

for i in minuman:
    for j in i:
        print (j)

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(minuman)):
    for j in range(len(minuman[i])):
        print(i,j,minuman[i][j], end=' ')
    print()

a=[1,2,3,4,5,6,7,8]
a.remove(4)
print(a)