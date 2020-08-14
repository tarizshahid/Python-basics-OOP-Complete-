import math
import sys
#single line comment
'''Multi
Line 
comment'''

#complex number
p = 3+2j
print(type(p))

#data type conversion
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
multiple input has two methods
lst = [input("Enter anything : ").split(',')] returns a list , values seprate by , 
OR
a,b,c = input("Enter three numbers : ).split('whatever you want to split by')'''

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


#OBJECT ORIENTED PROGRAMMING

#class
class Product:  # declare a class , use first letter "CAPITAL"
   
    def __init__(self):       #constructor built-in function (non-parameterized constructor)
        self.name = 'iPhone'  #define class data types
        self.description = "it's an awesome phone,atleast for some people"
        self.price = 25000
        
p1 = Product()
print('Product name :',p1.name,'\nProduct Desc. : ', p1.description,'\nProduct Price :', p1.price) #using class members via object (p1)

#parameterized Constructor
class University:
    
    def __init__(self , name , rating): #parameterized construtor
        self.UniName = name 
        self.Unirating = rating
       
u1 = University('FAST-NUU', 4.5) #pass values to parameterized constructor
print(u1.UniName,'\n',u1.Unirating)

#instance methods
class Evens:
    def __init__(self,number):
        self.value = number
    
    def avg(self): #defining instance method must use self , in static methods
        total = ((self.value+50)/2)
        return total

e1 = Evens(23)
print(e1.avg()) #calling an nstance method

#Getter & Setter methods
class Programmer: #we use setter getter when we dont use constructor to assign values
    
    major = "Computer Science" #define static field this way common for whole class and objects we can call it by object name and class name as well like Programmer.major and vice versa
    
    def setName(self,naam): #Setter
        self.name=naam
    
    def getName(self):     #Getter
        return self.name    

    def setSkill(self,tech):
        self.skill=tech
    
    def getSkill(self):
        return self.skill    
    
    def setSalary(self,maalu):
        self.salary=maalu
    
    def getSalary(self):
        return self.salary    
   
    def displayfun(self):
        print(self.name)
        print(self.skill)
        print(self.salary)
        
    
p1 = Programmer()
p1.setName("Somieeee")
p1.setSkill("Mere ko sub ata hai , me expert hoon")
p1.setSalary("999999")
print("Name : " , p1.getName() , "\nSkills : " , p1.getSkill() , "\nSalary : ",p1.getSalary())
p1.displayfun()

#class and static methods
class ClassMethods:
    
    Uni = 'FAST'          #defining static/class variables
    MaxScore = 3.5
    
    @classmethod          #use @classmethod decorator for class methods
    def Calc(cls , name , score):
        cls.avg = (cls.MaxScore/score)
        print("Name of Student : " , name , "\nName of University : " , cls.Uni , "\nScore : " , cls.avg) 
    
    @staticmethod # use @staticmethod for static methods
    def display():
        print("Static function display")
            
        
ClassMethods.Calc("Ali Zafar", 2.2) #can call class and static methods from class name and object name as well
ClassMethods.display()

#Inner Class (Class within class)
class Car:

    def __init__(self, name , model , price):
        self.name = name
        self.model = model
        self.price = price
    
    def display(self):
        print(self.name,self.model,self.price)
        
    class Engine: #class within class
            
        def __init__(self , engineNo , status=bool):
            self.engineNo= engineNo
            self.status = status
            
        def display1(self):
            print(self.engineNo ,self.status)    
                
C1= Car("BMW" , 2007 , 270000) #for outer class
C1.display()
E1=C1.Engine(127384 , True) #to access inner class we need object of outer class and then use inner class object to access inner class methods
E1.display1()

#Encapsulation  
class Student:            #Encapsulation is the process binding the methods and data/fields together so that only those methods can access that data

#private fields
    def __init__(self):
        self.__id = 1122   #here '__id , __name' are private fields , any field with '__' is private and cannot be accessed by object name (can be accessed by name mangling) 
        self.__name = 'Tariz Shahid'
    
S1 = Student()
print(S1._Student__name) #this is the name mangling , this is how we access the private fields outside class ,i.e (objectName._ClassName__PrivateField) 
print(S1._Student__id) 

#Implementing encapsulation
class Baby:  #This is how we implement Encapsulation (i) , (as we see private fields are still accessible by name mangling)
    
    def SetAge(self,age): #Mutator/Setter method as we did earlier
        self.age = age
    
    def GetAge(self):     #Accessor/Getter method s eariler
        return self.age

B1= Baby()
B1.SetAge(10)               #assigning values from outside class
print(B1.GetAge())          #Retrivng values outside class                           (This is how we implement encapsulation) (ii)
    
    
#Inheritance

class Car:
    def __init__(self,name,model,lic):
        self.name = name
        self.model = model
        self.lic = lic 
    
    def show(self):                                                              #when we inherit a class the child class also owns this method/funtion
        print('Funtion declared in CAR CLASS(show) , inherited by BMW')
    
    def Start(self):                                                             #Funtion for overriding
        print("simple method to show method overriding")           
        
            
class BMW(Car): #to inherit a class simply use class ChildClass(ParentClass):
    def __init__(self,Awards,EngineNo,name,model,lic):    #use parent class variables as weell as new variable of child class
        Car.__init__(self,name, model, lic)               #then call constructor of parent class 
        self.Awards= Awards                               #new fields of child class work this way
        self.EngineNo= EngineNo
        
        def Start(self):
            print("this show funtion overrided the parent Start function")          #now this is how funtion/method over-riding works
     
        
Bmw1=BMW(12,98345,'BMW_3rd_Series',2007,2918343333)
print(Bmw1.Awards,Bmw1.EngineNo,Bmw1.name,Bmw1.model,Bmw1.lic)
Bmw1.show()
Bmw1.Start()

#Super() funtion
class One:
    def __init__(self,prop):
        self.prop = None
        
    def mulFUN(self):
        print('parent class funtion (mulFUN)')
        
        
class Two(One):
    def __init__(self,memory,prop):
        super().__init__(prop)       #super will invoke the parent class (we dont use self when we invoke construtor of parent class via super())
        self.memory=memory
        
    def MulFUN(self):
        super().mulFUN()                  #here super acts like adding funtionality on existing funtionality   (super() refers to the parent class from which child s inherited)
        print('Child class funtion, (mulFUN)')
    
    
secondObj = Two(12,'4TB')
secondObj.MulFUN()                         #see in output it gives both output i.e from parent class and from child class method (mulFUN)

#Polymorphism                               #Polymorphism is the ability of an object to take on many forms
                                    
#Ducktyping   #type of polymorphism
class Duck:
    def talk(self):
        print('Quack Quack')
        
class Dog:
    def talk(self):
        print('Bark Bark')
        
def DucktypingObject(obj):
    obj.talk()   

duckobj = Duck()

dogobj = Dog()

DucktypingObject(duckobj) #duck typing example , for more google (ducktyping)

DucktypingObject(dogobj)  #duck typing  example  , i.e run time assigning object to funtion and it then calls the funtion of that object respectively

#Ducktyping for dependency Injection
class Flight:
    def __init__(self,engine):
        self.engine = engine
    
    def RUN(self):
        self.engine.start()
        
class AirbusEngine:
    def start(self):
        print('Starting AirBus Engine')
        
class BoingEngine:
    def start(self):
        print('Starting Boing Engine')
        
        
airobj = AirbusEngine()
FlightOBJ = Flight(airobj)   
FlightOBJ.RUN()                         #this is the beauty of duck typing we pass oject of any type and it invokes the start method of the respective object

BoingObj = BoingEngine()
FlightOBJ2 = Flight(BoingObj)
FlightOBJ2.RUN()                        #this is the beauty of duck typing we pass oject of any type and it invokes the start method of the respective object


#Operator Overloading
mylist =[1,2,3,4,5,6,7]
mylist2= [3,4,5,6,8,99,9]
print(mylist+mylist2)  #operator overloading

mystr = 'Evil'
mystr2 = 'bot'
print(mystr+mystr2)

#Abstraction                        #Abstraction means displaying only essential information and hiding the details

from abc import abstractmethod,ABC     #import this to use abstraction and inherit main class from class 'ABC'

class Parent(ABC):
    
    @abstractmethod                    #class with abstract method is an abstrat class, and classes we inherit from this class will be abstrct too until we implement the abcmeth0d in them
    def abcmeth0d(self):
        pass
        
class Child(Parent):
    
    def abcmeth0d(self):                # we cannot instantiate an abstract class , until we implement the abstract method present in it
        print('Implementation of abcmeth0d in child class')

    def __init__(self):
        pass

ccc = Child()
ccc.abcmeth0d()

#interface                 
 
'''interface is a class having all the methods == abstract methods , we cannot create object of interface'''
from abc import abstractmethod,ABC

class  TouchScreenLaptop(ABC):                     #interface
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):                         #Abstract class (no click() implementaion)
    def scroll(self):
        print('Scroll method HP') 
        
class DELL(TouchScreenLaptop):                       #Abstract class (no click() implementaion)
    def scroll(self):
        print('Scroll method DELL') 

class HPNotebook(HP):                               #complete implemented class
    def click(self):
        print('click method HPNotebook')

class DELLNotebook(HP):
    def click(self):
        print('click method DELLNotebook')
        
HPOBJECT=HPNotebook()
HPOBJECT.click()
HPOBJECT.scroll()

DELLOBJ= DELLNotebook()
DELLOBJ.click()
DELLOBJ.scroll()

