x=int(input('enter int value'))
for i in range(1,x+1):
    count=1
    for j in range(x,i,-1):
        if(j>x/2):
            print('a',end=' ')
        else:
            print('*',end=' ')
            if count==i:
                break
            else: 
                i=i+1

    print()