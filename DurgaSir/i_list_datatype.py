# Insertion order is preserved and duplicates are allowed
l=[]
print(type(l))
l.append(10)
l.append(20)
l.append(30)
l.append(10)
print(l)
l.append('Rakesh')
l.append(None)
print(l)
print(l[0],l[-1],l[1:4])
s=l*2
print(s)