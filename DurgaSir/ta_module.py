print("This is in module1")
x=10
y=20
def fun1():
    print('In function')
    if __name__=='__main__':
        print('The code is directly executed')
    else:
        print('The code executed from other module and __name__ is ',__name__)
fun1()