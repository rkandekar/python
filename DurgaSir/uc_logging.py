import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
# Default logging level is WARNING
print("Python logging demo")
logging.debug('DEBUG MESSAGE')
logging.info('INFO MESSAGE')
logging.warning('WARNING MESSAGE')
logging.error('ERROR MESSAGE')
logging.critical('CRITICAL MESSAGE')
logging.info('A new request')
try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print(x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with Zero')
    logging.exception(msg)
except ValueError as msg:
    print('Enter only int value')
    logging.exception(msg)
logging.info('Request message completed')
