#automatically it will evaluate, eval() takes string and evaluate
print(eval("1+2+3"))
expression=input("Enter some expression:")
result=eval(expression)
print(result)
#eval is smart will determine the variable type
x=eval(input("Enter one variable int or float or sting or any type:"))
print(type(x))
print(x)
for a in x:
    print(a)
