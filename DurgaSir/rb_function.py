#Default value for name is Guest if we do not pass name
#Default argument should be at last
def wish(msg,name='Guest'):
    return msg+name
print(wish('msg','name'))
print(wish('msg2'))