#Type casting
'''int(),float(),complex(),bool(),str()'''
print("Float to int:",int(123.456))
print(int(123.765))
#Cannot convert complex to int
#print(int(10+20j))
#Boolean to int
print("Boolean to int: ",int(True),int(False))
print("String to int:",int('50'))
#Float type conversion
print("Int to float:",float(10),"Cannot conver Complex to float:","Bool to float:",float(True),float(False),'String to float:',float('20'),float('25.6'))
print(round(10.64))
#Complex type conversion two type 1) complex(x)=x+0j 2) complex(x,y)=x+yj...x is real and y is imaginary
#in OOPS concept complex(x), complex(x,y) called overloaded function
print("Int to complex:",complex(10),"Float to complex:",complex(10.5),'Bool to complex:',complex(True),complex(False),'string to complex:',complex('35'))
print(complex(10,20),'bool to complex:',complex(True,False))
#For sting only pass one argument to complex() function complex("5","6") wont work
#Bool function
print(bool(0),bool(1),bool(2),bool(0.1),bool(0.0),bool(10+30j),bool(0+0j),bool('string'),bool(''))
#You can convert any type to String
print(str(10),str(10.5),str(True),str(19+32j))