
# coding: utf-8

# In[112]:

# Create socket
import socket
import sys


# In[113]:

try:
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print("\n","Houston we have a problem with the socket!")
    sys.exit() 


# In[114]:

#Connect to server
hostname = input("Enter a hostname to search, such as www.google.com ")
if hostname =="":
    hostname="www.google.com"
    
# Perform DNS lookup 
try:
    host = socket.gethostbyname(hostname) 
    print ("\n",hostname, "found at", host)

except socket.gaierror:
        print (host, "not found")
        sys.exit()

try:
    mysock.connect((host,80))
    
except socket.error:
    print("\n","Houston we have a problem with the socket!")
    sys.exit() 


# In[115]:

#Send request
#Generic http request
message = "GET / HTTP/1.1\r\n\r\n"

try:
    #Need to encode in python 3.5
    mysock.sendall(message.encode('utf-8'))
    
except socket.error:
    print("\n","Houston we have a problem with the socket!")
    sys.exit() 


# In[116]:

#Receive response 

try:
    # Include number of bytes to recevie to buffer
    data = mysock.recv(100000)
    
except socket.error:
    print("\n","Houston we have a problem with the socket!")
    sys.exit() 
    
print (data)


# In[117]:

#Close socket

try:
    mysock.close
    
except socket.error:
    print("\n","Houston we have a problem with the socket!")
    sys.exit() 


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



