#local variable and global variable
# Difference between Function(Group of statement),Module(Group of function),Package(Group of Module),Library(Group of Package)
#Recursive function
def fact(n):
    if(n>1):
        return n*fact(n-1)
    return 1
print(fact(2))

#Towers of hanoi