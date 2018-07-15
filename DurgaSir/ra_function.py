def emply(employee):
       return (employee+"LastName")
print(emply("Rakesh"))
emply('Kandekar')

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
# Positional argument
val=calc(10,2)
print(val)
# Keyword argument
print(calc(b=2,a=10))
# Valid positional followed by keyword argument
print(calc(10,b=2))
#multiple values for argument 'a'
# print(calc(2,a=2))