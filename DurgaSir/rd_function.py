#Positional arg with variable length argument
def fun(name,*n):
    print(name,n)
fun('Rakesh')
fun('Kandekar',1)
fun('RakeshKandekar',1,2,3,4)
 
def fun2(*n,name):
    print(n,name)
fun2(name='Rakesh')
fun2(1,name='Kandekar')
fun2(1,2,3,name='RakeshKandekar')