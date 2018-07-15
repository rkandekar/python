#print(input("enter the input variables:"))
a=int(input("enter one int"))
b=int(input("enter another int"))
print(a+b)
# read multiple input in single line
x,y=[float(m) for m in input("enter 2 float value:").split()]
print(x+y)
l,m = [int (x) for x in input("Enter two int with ',' saperator:").split(',')]
print(l,m)

#End with new line or any character
print('Line one',end=(','))
print('Start second line')