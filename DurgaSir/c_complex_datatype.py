# Complex number format a+bj (a=real part, b=imaginary part, j^2=-1)
# real part can be decimal, binary, octal and Hexadecimal but imaginary part has to be only decimal (int or float)
# a, b can both be int or float value
x=10+20j
print(type(x),x)
print(x.real,x.imag)
print("Real type:",type(x.real),"Complex type:",type(x.imag))
y=10.5+30.4j
print(type(y),y)
print("Add complex",x+y,"\n"+"Substract complex",x-y,"\n"+"Multiply complex",x*y,"\n"+"divide complex",x/y)
z=0B11101+25j
m=0X3434+20j
print(z+m)
print(type(z.real))
