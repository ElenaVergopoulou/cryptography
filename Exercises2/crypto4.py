def repeatedSquaring(a,n,m):
    x=a%m
    y=1
    while (n>0) :
        if (n%2 != 0):
            y=(y*x)%m
        x=(x**2)%m
        n=n//2
    return y

def fermat(a,iter):
    w=2
    for _ in range(iter):
        if  (repeatedSquaring(w,a-1,a) != 1) :
            return False
        w+=1
    return True

for i in [67280421310721,170141183460469231731687303715884105721,(2**2281)-1,(2**9941)-1,(2**19939)-1]:
    if (fermat(i,10))==True:
        print("Its a prime")
    else:
        print("Its not a prime")
#(True,False,True,True,False)
