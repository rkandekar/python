l=[1,2,3,4]
def funDouble(x):
    if(x%2==0):
        return x
l2=list(filter(funDouble,l))
print(l2)

l3=list(filter(lambda x:x%2==0,l))
print(l3)
