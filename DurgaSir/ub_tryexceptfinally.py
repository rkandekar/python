try:
    try:
        print("Inner try")
        print(10/0)
    except:
        print('inner except')
    finally:
        print('inner finally')
except:
    print('outer except')
finally:
    print('outer finally')