import socket
from datetime import datetime
net = input("Enter the IP address: ")
net1 = net.split('.')
_ = '.'

net2 = net1[0] + _ + net1[1] + _ + net1[2] + _
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr, 135))
   if result ==0:
      return 1
   else:
      return 0
      
def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      try:
         if (scan(addr)):
            print (addr , "is live")
      except:
            print(addr, "is off")
         
run1()
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: " , total)
