x=int(input('Enter any number'))
y=[1,2,3]
for j in range(1,x+1):
    print('* '*j)
print()
for i in range (1,x+1):
    for j in range (1,i+1):
        print('*', end=' ')
    print()
print()
for i in range (x,0,-1):
    print('* '*i)
print()
for i in range(x,0,-1):
    for j in range(0,i):
        print('*', end=" ")
    print()
print()
