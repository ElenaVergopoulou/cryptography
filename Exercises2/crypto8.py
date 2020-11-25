def repeatedSquaring(a,n,m):
    x=a%m
    y=1
    while (n>0) :
        if (n%2 != 0):
            y=(y*x)%m
        x=(x**2)%m
        n=n//2
    return y

def superExp(a,n,tupl):
    t,f=tupl
    if n==0:
        return 1
    if (t==0 and f==0):
        return 0
    elif f==0 :
        nt=t-1
        nf=f
    else:
        nt=t+1
        nf=f-1
    return repeatedSquaring(a,superExp(a,n-1,(nt,nf)),(2**t)*(5**f))

def superExpWrapper(a,n,digits):
    return superExp(a,n,(digits,digits))


print(superExpWrapper(1707,1783,16))

