#downloading HTML
import urllib.request
#try:                                                                           #using this in case url not found 
    #url = urllib.request.urlopen("https://www.python.org/")                    #loading url
    #content = url.read()                                                       #read the content of url
#except  urllib.error.HTTPError:                                                #in-built module which deals url not found
    #print('URL not found')
    #exit()                                                                     #Program exit 
    
#f = open('python.html','wb')
#f.write(content)                                                               #commenting because it writes the file everytime I run the code , uncomment accordingly
#f.close()

#Downloading Image
url = 'https://www.python.org/static/img/python-logo.png'
#urllib.request.urlretrieve(url, 'python.png')                                  #parat=meters : 1) URL tp grab image from , 2)filename     (extension can be same as in url or any other accordingly)

#Socket Programming

#Creating a Server (TCP/IP)
import socket
host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        #AF_INET for IPv4 , and SOCK_STREAM for TCP/IP communication , these values are default even if we don't specify them or we can say we can use socket.socket() , (s is socket object)
s.bind((host,port))                                                          #bind() accepts paramteres in the form of set , so we pass host and port
s.listen(1)                                                                  #parameter 1 here means how any clients can connect to server
print("Server listening on port : " , port)
con , addr = s.accept()                                                      #used to accept the client connection, returns two things i)Connection ii)address from which the request came from/client address  
print('Connection from :' , str(addr))                                       #convert address object to string to show address from where request is coming or client address
con.send(b"Hello , Welcome to the Server")                                   #used to send anything to client , here we send a string converted into binary using 'b' in start of string
con.send('United we stand divided we fall'.encode())
con.close()

#Creating a Client
soc = socket.socket()                                                         #creating a socket to recieve messages
soc.connect((host,port))                                                      #connect() also accepts parameters in form of set
msg = soc.recv(1024)                                                          #1024 is the buffer size , means how much data we recieve at a time , first message recieved
    
while msg:                                                                    #loop to recieve messages continuously
    print("Recieved ..." , msg.decode())                                      #we have to decode the message as we encoded on server side
    msg = soc.recv(1024)
soc.close()

#File server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        
s.bind((host,port))                                                          
s.listen(1)                                                                  
print("Server listening on port : " , port)
con , addr = s.accept()
fileName = con.recv(1024)                                                      #read name of file which client says
try:                                                                           #handling exception in case the file not found 
    f = open(fileName,'rb')                                                    #opening that file in read binary mode(rb)
    content = f.read()                                                         #reading content of file 
    con.send(content)                                                          #sending content to client
    con.close()                                                                #closing connection
except FileNotFoundError:
    con.send(b"File doesn't exist")
con.close()

#File client
soc = socket.socket()                                                         #creating a socket to recieve messages
soc.connect((host,port))                                                      #connect() also accepts parameters in form of set
fileName = input("Enter file name : ")                                        #Getting file name from client
soc.send(fileName.encode())                                                   #sending file name to server
content = soc.recv(1024)                                                      #recieving file content
print(content.decode())
soc.close()

#Sending Emails                                                               (smtp server)
import smtplib
from email.mime.text import MIMEText

body = "This is a test EMAIL , How you do'in?"
msg = MIMEText(body)
msg['From'] = 'f180263@nu.edu.pk'
msg['To'] = 'tarizshahid@gmail.com'
msg['Subject'] = 'Test Mail'
server = smtplib.SMTP('smtp.gmail.com',587)                               #smtp gmail server and port
server.starttls()
server.login('EmailAccountHere','PasswordHere')                           #login , id , password
server.send_message(msg)                                                  #send msg to desired email
print("Mail sent")
server.quit()
