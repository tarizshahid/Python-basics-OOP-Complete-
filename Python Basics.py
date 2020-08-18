import math
import sys
#single line comment
'''Multi
Line 
comment'''

#complex number
p = 3+2j
print(type(p))

#data ype conversion
flo = 4.3
flo =int(flo)
print(flo)

#string
A1 = '''MULTI
LINE
STRING'''
A2 = 'single string'
print(A1[3]) #print 3rd index
print(A2*4) #print string 4 times
print(len(A2)) #prints length of container/string

#slicing
str1 = '    123456789    '
print(str1[2:5]) #slice the string : arguments = [starting index : ending index]  IMP: it doesn't include the ending index in output
print(str1[-3:-1])  # prints from -3 ----- -1(-1: last index OR first index from right) here it will also not include ending index
print(str1[0:9:2]) #3rd argument here is for step it means it will jump 2 steps then print
print(str1[8::-1]) #starting from ending index , going to first index , with a step of -1 means it will REVERSE the string
print(str1[::-1]) # reverse string using slicing

#string methods
print(str1.strip()) #removes space from the string , use lstrip to strip left spaces and rstrip for vice versa
print(str1.find('3', 0 , 10)) #returns index of string at which it's found here 0 , 10 (optional) are starting and ending index which means look in b/w these indexes (returns -1 if not found)
print (A1.count('I')) #counts the number of a sub-string that occurs in a string
print (A1.replace('LINE', 'todo')) # replace the substring ('old','new') 
print(A2.upper()) #to upper case
print(A2.lower()) #to lower case
print(A2.title()) #To Title Case Of String

#LIST
lst = [1,22,65,98,23,123,12334,-132]
print(lst) #len() , duplication , Slicing , steps in slicing , accessing by index in lists are same as of strings etc
print(min(lst)) #prints minimum value in list (type must be same to compare no comparison b/w string and int)
print(max(lst)) #prints maximum value in list (type must be same to compare no comparison b/w string and int)
lst.sort() #sorts in ascending order use lst.sort(reverse=True) for descending order
print(lst)
lst.append('blah blah') # adds value to the end of list
print(lst)
lst.remove(123) #remove by value (lst.clear() removes all elements from list)
print(lst) 
del(lst[3]) #del built-in funtion to remove value by index
print(lst) 
lst.insert(3,'Ali') #insert at specific index
print(lst)

#tuple  (LIST that cannot be modified , when list/tuple have one element use a comma e.g lst = [20,] OR tpl = (42,) 
tpl = (1,3,45,65,76,12,'Tariz')
print(tpl) #tuple has not much funtions we can perform , indexing, count, repetition ,min,max,len funtions on tuple which dont modify it
lst1 = [11,22,33]
tpll = tuple(lst1) # convert list to tuple

#sets [
set1 = {1,2,34,5,67,8,1,2,34}
print(set1) #(don't have repeated values) 
set1.add(12) #used to update one value 
set1.update([22,56,76,99]) #used to update multiple values and they dont have any order
print(set1) #cannot perform indexing ,repettion , slicing/subscripting etc because no indexes in sets
f = frozenset(set1) #converts simple set to frozen set which means a set cannot be modified now
r = range(5) #starts from 0 go to given-1 i.e here 0,1,2,3,4 & range(1,12,3) first : start , second : end(i.e end-1) , third : steps

#bytes
lst1122 = [24,56,32,5,6,9,87]
b=bytes(lst1122) #bytes cannot be modified neither can be indexed, no slicing , value b/w (0 ,256)
print(type(b))
lst22 = [14,57,31,51,6,9,87]
bArray= bytearray(lst22) #value b/w 0,256 cannot be sliced but index use possible
bArray[2] = 23
print(bArray)
print(type(bArray))

#Dictoionary
dic1={1:'Ali' , 2:'Salim' , 3:'Tariz'}
print(dic1.items()) #prints all stuff in a disctionary
print(dic1) #prints all stuff in a disctionary
key = dic1.keys() #returns a set of keys in dictionary to be itrated by loop
for i in key:
    print(i)
value = dic1.values() #returns a set of values in dictionary to be itrated by loop
for i in value:
    print(i)
print(dic1[2]) #here 2 is the key not the index

#operators
#+ , - , / , * , **
# < , > , <= , >= , == , !=
# and , or , not
a , b = '++++' , '----'
print(a, b ,sep='8888888888') #sep = seprates them by given symbol

#string
gpa = 3.0
name = 'evilbot'
print ("name is" , name , "CGPA is " ,gpa)

#input
'''inp = int(input("Enter message here to display : )) default input() is string , use whatever you need in input
multiple input has many methods
lst = [input("Enter kro kuch : ").split(',')] returns a list , values seprate by , 
OR
a,b,c = input("Enter three numbers : ).split('whatever you want to split by')    here type of a,b,c will be class <str>
OR 
by loop'''

#Break - Continue
'''same as C++'''

#command Line arguments
'''arguments that are passed to a program at runtime , either be a database connection string , IP to scan , filename/filepath etc
passed via a list name as sys.argv(module:sys)'''
arguments =  sys.argv
for i in arguments:print(i)

#functions
def calc(a,b): #funtion defination
    x=a+b
    y=a-b
    z=a*b
    c=a/b
    return x,y,z,c #return all values as a tuple

print(calc(10,5))  #funtion calling also call as calc(a=10,b=5)
'''to use global variable in a funtion use globals()['name of variable'] , we can assign a funtion to variable like co = calc and call it as co(x,y i.e arguments)
if a funtion is nested it can be only used within the parent function not globally , we can return child functions as a result of parent fucntion too'''

#lambdas (anonymous small functions)
f = lambda val: val*val #returns a square of number
print(f(2)) #calling lambda
lam = lambda var1 : 'even' if var1%2==0 else 'odd' #if else in lamba work this way
print(lam(3))
lisst = [1,2,3,4,5,6,67,8,9,9,12,34,56,78,9,54,3,21,11,33,35]
evenn = list(filter(lambda lol: lol*2  , lisst)) # filter function filters an object/list on the basis of lambda funtion, every result passes to a new filter whih return true for the filter funtion ,as this funtion returns a filter type then we convert it into list type
print(evenn) #prints a list whcih contains only even numbers , 
evenn1 = list(map(lambda lol: lol*2  , lisst)) #map function applies the funtion given in lambda on all members of list/object given in this case it will double the values in 'lisst'
print(evenn1)

#modules
from math import * #imports all funtions no need to write math.sqrt simply write sqrt() and so on
'''import 'myModule' as Ma , it will help to use Ma.fun() instead of myModule.fun()
we can create our own moudles too easy''' 

#list comprehensions
newlist = []
newlist = [var12**2 for var12 in range (1,11)]  # this is how list coprehensions work
print(newlist) 
evlist = []
evlist = [eve for eve in range(1,21) if eve%2==0] #another example
print(evlist)

#Random number generation
import random

for i in range(10):
    print(random.randint(1,100))
