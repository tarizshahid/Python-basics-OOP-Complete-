#Simple try except block

try:
    #a,b = input('Enter twoo numbers, sperated by comma : ').split(',')   #if error occurs here i.e zero division then except block will execute, i.e exception is raised
    #c = int(a)/int(b)
    #print(c)
    pass
except ZeroDivisionError:
    print('Division by zero is not possible')

#use of Finally
try:
    f = open('filename', 'w')
    #a1,b1 = input('Enter twoo numbers, sperated by comma : ').split(',')
    #c1 = int(a1)/int(b1)
    #print(c1)
    f.write('writing to file :  whatever  you want to write')                            #if we dont use finally and error occurs in try block , the file will remain open, so we use finally where error occurs or not but we need to execute those lines of code
except ZeroDivisionError:
    print('Division by zero is not possible')
else:
    print('you entered a non-zero number for diviison (we"re in else block)')                #it runs when no excption is raised
finally:
    f.close()
    print('file closed')
print('code after execption')


#Logging

import logging   #must import thsi module for logging , root logger is the logger which gives us logging information

logging.basicConfig(filename='mylogfile.log' ,level=logging.DEBUG)        #to log into file(file extension must be .log) and default level , if we use Debug here we see all logs above debug and debug too, same if we use error we see error and critical but nothing below, level must be in upper case (e.g logging.ERROR)
logging.critical('Critical')              #above warning
logging.error('Error')                    #above warning
logging.warning('Warning')                #default log level
logging.info('info')                      #below warning
logging.debug('Debug')                    #below warning


#Assertions                              #assertions are used for input validation

'''num = int(input('Enter even number : '))
assert num%2==0 , 'You entered a non-even number'                    assert variableName(condition as i checked for even) , if condition fails then show this string after comma'''

try:
    numbr = int(input('enter an odd number : '))                                #handle assertions in a better way
    assert numbr%2!=0 , 'You entered an even number'
except AssertionError as obj:
    print(obj)

print('after assertion')



#simple Invalid password length custom exception

class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg
        
def Pas(password):
    if (len(password) < 8):
        raise InvalidPasswordException("Password length is less than 8 characters")

pwd = str(input("Enter the password:"))
try:
    Pas(pwd)
except InvalidPasswordException:
    print("Password length should be atleast 8 characters")
else:
    print("Accepted Password Length")
finally:
    print("Code after exception")