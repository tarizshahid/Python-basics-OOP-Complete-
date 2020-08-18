#File Handling
'''
f=open('filename','mode','buffer')  , buffer is optional argument here

                        File modes
                        
1)  w (write mode,deletes all items in file and write new stuff in it)
2)  r (read mode , to read file)
3)  a (append mode , write to file but previous data is not removed)
4)  w+ (write and read)
5)  r+ (read,write and append)
6   a+ (appen and read)
7)  x  (exclusive mode ,  new file created exclusively , if a file exists with same name error occurs)

Note : these modes are for text files , for binary files like images,audio etc we use 'b' at the end of mode name , i.e wb,rb,ab and so on'''
 
#writing string to file

#f=open('simpleFile.txt','w')
#inn = input('Enter a sentence to write to file : ' )
#f.write(inn)                                           #it will write the string in 'inn' to file simpleFile.txt, commenting it because asks for input everytime you run
#f.close()

#reading from file
f=open('simpleFile.txt', 'r')
print(f.read())                          #read from file
f.close()

#writing multiple strings to file

#f=open('simpleFile.txt', 'w')
#print("Enter anything you want (type $ and press enter when you're done")
#s=''
#while s!='$':
#    s = input()
#    f.write(s)
#f.close()

#check if the file exists

import os,sys            #import these two modules must

if os.path.isfile('simpleFile.txt'):
    print('File Exists')
else:
    print("File doesn't exist")
    sys.exit()

#pickle module                             #to dumb object to file

import pickle

class Student:    
    def __init__(self,name, age,id):
        self.name = name
        self.age = age
        self.id = id
    
    def check(self):
        print('callling function from returned file object')
    
    def dsiplay(self):
        print(self.name)
        print(self.age)
        print(self.id)
        
s =Student("Ali",17,28960)
f= open('Student.dat','wb')    #wb beacuase its a binary file as we pass an object into it , dat extension means data
pickle.dump(s,f)               #object name & file
f.close()

#unpickle

f = open('Student.dat','rb')         #filename , and read mode and file is binary so rb
obj = pickle.load(f)                 #picle.load(file object)
obj.check()
obj.dsiplay()