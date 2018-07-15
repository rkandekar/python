a=10
b=20
c=30
d=True
if a>b :
    print("a is greater than b")
else:
    print("b si greater than a")

#chaining of relational operator. If atleast one is False result is False. All comparition has to True to get True
print(a>b>c)
print(a<b<=d,(a<b)<=d,True<=d)
print(10<20<30<40,10<20<30<40>70)

#Equality operator (==, !=). Chaining operator is allowed for equality operator
print(10==20,10!=20)
print(10==20==30==40,10==5+5==7+3)
print(1==True)
#logical operator and,or,not (Can apply eith for Boolean or non Boolean type) (For non Boolean returns non boolean)
#Non zero is True and Zero is False
print(True and True, True or False, False or True, False and False, False or False)
print(10 and 20)