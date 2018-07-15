# Ways to print output
print()
print("string variable")
a,b,c=10,20,30
# Default saperator is space and default end is new line char
print("stringa aba acd with no sep",a,b,c)
print("stringa aba acd with sep",a,b,c,sep=' ')
print("line one input sepoperator",a,b,c, sep=',')
print('first line',end=(','))
print('second line')
#escape char
print('escape character in string \n to check new line')
print("concat1"+"concat2")
print("str1","str2")
lst=[a,2,2,4]
tup=('a','s','f','get')
setval={1,2,3,4}
dicval={1:'val',2:'val2'}
print(lst,tup,setval,dicval)
#format string
print("list value is:%s, tuple value is %s,setval is :%s,dict is:%s" %(lst,tup,setval,dicval))
#replacement operator {}
print("list value is:{0}, tuple value is {1},setval is :{2},dict is:{3}".format(lst,tup,setval,dicval))
print("list value is:{}, tuple value is {},setval is :{},dict is:{}".format(lst,tup,setval,dicval))
print("list value is:{x}, tuple value is {y},setval is :{z},dict is:{a}".format(x=dicval,y=lst,z=tup,a=setval))