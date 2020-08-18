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

