from imp import reload #This will work to reload module
import ta_module
import time
#time.sleep(30)
import ta_module #This wont work to reload latest module
reload(ta_module) #This will work to relad module
print('In module 2')
module2_a=0
print(dir()) # to find members of module
print(dir(ta_module))
print(ta_module.fun1())