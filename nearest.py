def nearest(a1,a2,n,c,k,l,ch):
    for i in range(len(a1)):
        if(i not in c):
            if(not(a1[i]<a2[k])):
                t=n
                print(i,k,)
                b=c[:l+1]
                c.append(i)
                b=c[:l]
                n=n*10+a1[i]
                if(a1[i]>a2[k]):
                    for j in range(len(a1)):
                        if(j not in c):
                            n=n*10+a1[j]
                            print(n)
                    return n
                k=k+1
                if(l<len(a1)-1):
                    g=nearest(a1,a2,n,c[:],k,l+1,ch)
                    c=b
                    if(g>ch):
                        return g
                    k=k-1
                    n=t
                else:
                    if(n>ch):
                        return n
                    return -1
        if(i==len(a1)-1):
            return -1

a=list(map(int,input().split()))
b=a[0]
d=a[1]
a1=[]
a2=[]
while(b!=0):
    r=int(d%10)
    r2=int(b%10)
    a1.append(r2)
    a2.append(r)
    d=int((d-r)/10)
    b=int((b-r2)/10)
a1=sorted(a1)
a2=a2[::-1]
g=nearest(a1,a2,0,[],0,0,a[1])
print(g)
