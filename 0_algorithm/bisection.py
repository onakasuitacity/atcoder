# bisection (O(r-l))
def bisection(l,r,f,discrete=True,left=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return h if not discrete else l if left else r

# example
print(bisect(-4.2,10.2,lambda x:x>6.5,discrete=False,left=False))
