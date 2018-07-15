#Variable length argument
def sum(a,b):
    print(a+b)
sum(1,2)
#I cant use sum(1,2,3)
# To overcome use variable length argument
def sumv(*n):
    pass
print(sumv())
print(sumv(1))
print(sumv(1,2))
# *n is group of value, and n will become Tuple
# To print sum of given numbers
def f1(*n):
    print("variable arg function")
    sum=0
    for x in n:
        sum=sum+x
    print(sum)
f1()
f1(10)
f1(10,20,30)