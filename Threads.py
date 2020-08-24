'''So far we written code which was single threaded , we use threads to use best of processor and also improving performance. we create threads which runs in parallel
three ways to create multiple threads:
1) using functions e.g t=Thread(target=funtionName,funtionArguments) , then we call t.start() to execute
2) Extend the thread class
3) Hybrid approach 
'''

#Main thread

import threading                                                                           #threading module to implement multi-threaded programming
print("Current thread that is running : " , threading.current_thread().getName())          #gets the name of current thread

#to check if it's a main thread or not
if(threading.current_thread()==threading.main_thread()):
    print("we're in Main Thread")
else:
    print('some other Thread')
    
#Thread using funtion
from threading import Thread                                                            #a class in threading module to spawn off our thread

def DisplayNumbers():                                                                   #A simple funtion printing first 10 numbers
    i = 1
    print(threading.current_thread().getName())
    while(i <= 10):
        print(i)
        i+=1

print(threading.current_thread().getName())
t = Thread(target=DisplayNumbers)                                                          #Pass the funtion to constructor of thread class as done here
#t.start()                                                                                 #to start the tread object use ThreadObjectName.start()

#Thread , extending the Thread class
class MyThread(Thread):                                                                     #inheriting myThread from class thread
    def run(self):                                                                          #overriding the run method in Parent class i.e Thread 
        i = 1
        while(i <= 10):
            print(i)
            i+=1

Obj = MyThread()
#Obj.start()             #Don't use obj.run() because it won't invoke new thread it will run in main thread, as we know obj is of type thread so we have to use start() to create new thread , it will invoke the run() automatically

#Thread , without using parent Thread class (Hybrid Approach)
class ThreadClass:
    def fun(self):
        i = 10
        while (i>=1):
            print(i)
            i-=2
        
        
obj = ThreadClass()
t = Thread(target=obj.fun)
#t.start()                                                              #commenting the start statements because threads run in paralle so the output is interrupted

t2 = Thread(target=obj.fun)                                             #when we run multiple Threads in one program like this it is called multi threading and output depends on Python Thread scheduler , the output can be adjusted by using sleep() from time module
#t2.start()                                                              

t3 = Thread(target=obj.fun)
#t3.start()

'''
                            --------------Notes------------
Thread synchronization is the concurrent execution of two or more threads that share critical resources.
Threads should be synchronized to avoid critical resource use conflict
We can lock an object using:
1) Lock
2) Semaphores

When a Thread locks an object it enters a room of it's own, Only when the Thread releases that object, other Threads can use it. This process of Thread accuqiring a lock and entering a room is aso known as Thread Mutex 
Lock process is as follows:
obj = Lock()         (oBj is of class thread.lock type)
obj.acquire()        (Thread will acuqire lock on current object)
obj.release()        (No other Thread can use this obj until the given statement is executed)

Semaphore:
Semaphore is just acuqiring a lock but internally it uses a counter. initially the number is one(1), 
Everytime a lock is acquired its value is decremented by one(1)
Everytime a lock is released its value is incremented by one(1)

obj = Semaphore()    (obj is of class threading.Semaphore type)
obj.acquire()        (Thread will acuqire lock on current object)
obj.release()        (No other Thread can use this obj until the given statement is executed)

'''
from threading import Lock                                                                    #to use synchronizaion with Lock()

#Ticket Booking usecase (with synchronization)
class Bus:
    def __init__(self,AvailableSeats):
        self.AvailableSeats = AvailableSeats
        self.lock = Lock()     #for sync using semaphore use self.lock = Semaphore(), all other process is same i.e acquire() and release() , Lock object to implement synchronization,
             
    def buy(self,ticketsNeeded):
        self.lock.acquire()                                                                     #acuriring lock
        print("Available tickets are : ", self.AvailableSeats)
        if(self.AvailableSeats>=ticketsNeeded):
            print('\nConfiriming Seat...')
            print('\nSeat Confirmed , printing the Ticket...')
            self.AvailableSeats-=ticketsNeeded
        else:
            print('Sorry, NO Seats Available')
        self.lock.release()                                                                     #releasing lock                    

from time import sleep
obj = Bus(10)

th1 = Thread(target=obj.buy,args=(3,))                             #In threads , to pass arguments to function we use this method,internally Thread class expects it as a list so it can be iterated , adding comma at the end makes a list i.e 3, is a list 
th1.start()

th2 = Thread(target=obj.buy,args=(3,))
th2.start()

th3 = Thread(target=obj.buy,args=(6,))
th3.start()


#Thread Communication using flag (Consumer/Producer case)
class Producer:
    def __init__(self):
        self.products = []
        self.orderPlaced = False
    
    def produce(self):
        for i in range(1,6):
            self.products.append('Product'+str(i))
            sleep(1)
            print("item Added")
        self.orderPlaced = True

class Consumer:
    def __init__(self,prod):
        self.prod = prod
        
    def consume(self):
        while (self.prod.orderPlaced == False):
            print("Waiting or order ...")
            sleep(0.5)
        print('Orders shipped',self.prod.products )

P = Producer()
C =  Consumer(P)

t1 = Thread(target=P.produce)
t2 = Thread(target=C.consume)
#t1.start()
#t2.start()

#Thread commuication using wait and notify
'''
wait , notify , notifyAll are methods available in class Condition
'''
class Producer1:
    def __init__(self):
        self.products = []
        self.L = threading.Condition()                               #Threading.condition object
            
    def produce(self):
        self.L.acquire()                                               #locking the object
        for i in range(1,6):
            self.products.append('Product'+str(i))
            sleep(1)
            print("item Added")
        self.L.notify()                                                #Notify other thread that task is completed
        self.L.release()                                               #Releasing object

class Consumer1:
    def __init__(self,prod):
        self.prod = prod
        
    def consume(self):
        self.prod.L.acquire()
        self.prod.L.release()
        print('Orders shipped',self.prod.products )

P = Producer1()
C =  Consumer1(P)

t1 = Thread(target=P.produce)
t2 = Thread(target=C.consume)
#t1.start()
#t2.start()
