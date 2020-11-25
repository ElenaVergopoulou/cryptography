import math

def Expo(Z,M):
    c=0
    if math.gcd(Z,10**M)==1:
        if M==1:
            c=4
        else:
            c=10**M*2//5
            w=pow(1998,100**10,c)
            x=pow(1000,100**10,c)
            y=(x*y)%c
            res=pow(Z,y,10**M)
    else:
        res=pow(Z%(10**M),1998*1000)%(10**M)
        res=pow(res,100)%(10**M)
        res=pow(res,10)%(10**M)

    return(res)

print(Expo(548,3))
