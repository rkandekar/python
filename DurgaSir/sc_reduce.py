import functools
from functools import reduce

l=[1,2,3,4]
def sum(l2):
    sum=0
    for x in l2:
        sum=sum+x
    return sum
print(sum(l))

def greater(x,y):
    if x>y:
        return x
    else:
        return y
print(greater(3,4))
f = lambda a,b: a if (a > b) else b
print(functools.reduce(f, [47,11,42,102,13]))


lam=lambda a,b:a if (a>b) else b
#maxval=reduce(lam,l)
#l2=reduce(sum,l)
#print(l2)