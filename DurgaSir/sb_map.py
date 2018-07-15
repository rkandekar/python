l=[1,2,3,4]
def funDouble(x):
   return x*2

l2=list(map(funDouble,l))
print(l2)

l3=list(map(lambda x:x*2,l))
print(l3)