#DateTime today

import datetime                      #module to import

dt = datetime.datetime.now()         #gives current time we can use today()/now()
print(dt)                            
print(dt.day,dt.month,dt.year)       #can retrive day monts hour year seprately too
print(dt.hour,dt.minute,dt.second)

#beautify the output
print('Current date : {}/{}/{}'.format(dt.day,dt.month,dt.year))
print('Current time : {}:{}:{}'.format(dt.hour,dt.minute,dt.second))

#Combining date & time
from datetime import *
d = date(2020,10,5)                   #date object
t = time(11,25)                       #time object
dt = datetime.combine(d,t)            #combined as datetime.combine(dateobject,timeobject)
print(dt)

#Sorting dates
mylist = []
d1 = date(2012,7,3)
d2 = date(2018,5,22)
d3 = date(2020,7,11)
d4 = date(2010,11,18)
d5 = date(2007,7,29)
mylist.append(d1)
mylist.append(d2)
mylist.append(d3)
mylist.append(d4)
mylist.append(d5)
print("List before sorting date :")
for d in mylist:
    print(d)
mylist.sort()                      #sort the date objects in list
print("after sorting :")
for d in mylist:
    print(d)
    

#Sleep()
import time
mylist = []
for i in range(65,91):
    mylist.append(chr(i))

print('program in sleep for 3 seconds ...\n')
time.sleep(3)                                   # sleep funtion for delay in programs
for i in mylist:
    print(i)

#Knowing Execution time or program

startTime = time.perf_counter()             #this line at the start of your code
print("Executing code...")
time.sleep(5)
endTime = time.perf_counter()
timeTaken = endTime - startTime
print('Time taken by our code for execution is : ', timeTaken)                   #it will be around 5 seconds a swe used sleep(5)
