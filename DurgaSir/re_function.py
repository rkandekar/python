#Keyword variable length arguments ** it will become dictinalry
def display(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k,'.......',v)
display(name='Rakesh',number=1,age=30)

def f1(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f1(3,2)
f1(10,20,30,40)
f1(25,50,arg4=100)
f1(arg4=2,arg1=3,arg2=4)
#below not allowed
#f1(arg3=10,arg4=40,20,30)
