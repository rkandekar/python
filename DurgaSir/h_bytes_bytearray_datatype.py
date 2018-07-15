# to represent binary data like images, video files and audio files
#bytes must be in range(0, 256)...bytes is immutable 
x=[10,20,30,40]
print(x,id(x))
b=bytes(x)
print(type(b))
for a in b:
   print(a)
print(x[0],b[0])
#Byte array data type...bytearray is mutable you can change the value...butin range(0, 256)
y=[11,12,13,14]
c=bytearray(y)
print(type(c))
print(y[0],c[0])
c[0]=111
print(y[0],c[0])