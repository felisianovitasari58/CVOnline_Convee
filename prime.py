# buat fungsi utk mereturnkan apakah bil inputan adlh bil prima atau bukan

def prime(bilangan1):
    a=0
    for i in range(1,bilangan1+1):
        if(bilangan1%i==0):
            a+=1
    if(a==2):
        return True

a=int(input('brp: '))
if (prime(a)==True):
    print("bil prima Loh")
else:
    print("bukan prima loh")