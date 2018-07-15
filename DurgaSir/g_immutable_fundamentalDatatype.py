# Everythin in python is an object
# All fundamental data type are immutable.
''' int, float, complex, bool, string are all fundamental data type and are immutable (cannot be changed in memory)'''
a=10
print("address of a:",id(a),"value of a:",a)
a=20
b=20
c=20
print('After change address of a:',id(a),'value of a:',a)
print("address of b:",id(b),"value of b:",b)
print("address of c:",id(c),"value of b:",c)
# here both a and b have same value so only one memory object is created with two reference variable in Python increases the performance 
b='z'
print("b is changed to string address of b:",id(b),"value of b:",b)
print(a is c) # is operater checks if its pointing to same object
x=10
y=10
print ("x address:",id(x),"y address:",id(y))
x=256
y=256
print ("x address:",id(x),"y address:",id(y))
x=123456
y=123456
print ("x address:",id(x),"y address:",id(y))
print(x is y)
m=10383.20
n=10383.20
print ("m address:",id(m),"n address:",id(n))
print(m is n)
complex_a=10+20j
complex_b=10+20j
print(id(complex_a),id(complex_b))
print(complex_a is complex_b)
