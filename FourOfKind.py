# cara satu
increment=0
kartu=["2w","2k","2h","2s","3w","3k","3h","3s","4w","4k","4h","4s","5w","5k","5h","5s","6w","6k","6h","6s","7w","7k","7h","7s","8w","8k","8h","8s","9w","9k","9h","9s","10w","10k","10h","10s","Jw","Jk","Jh","Js","Qw","Qk","Qh","Qs","Kw","Kk","Kh","Ks","Aw","Ak","Ah","As"]
arrtemp=[]
for i in range(0,52,4):
    for j in range(i,i+4):
        arrtemp.append(kartu[j])
    for k in range (52):
        if(arrtemp[1][0]!=kartu[k][0]):
            arrtemp.append(kartu[k])
            print(arrtemp)
            arrtemp.remove(kartu[k])
            increment+=1
    arrtemp.clear()
print("Kombinasi: ", increment)
