import os 
import time
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
  
if shutdown == 'y' or shutdown == 'Y': 
    info = input(" Now (yes / no): ") 
    if info == "y" or info=="Y":
    	print("Y")
    	os.system("shutdown /s /t 1")
    	print(f"Bye Bye")
    	time.sleep(1)
    else:
    	info2 = int(input("How many minuets leter ? ") 	)
    	try:
    		print(f"You will be shutdown after {info2} minuets")
    		os.system(f"shutdown /s /t {info2*60}")
    		time.sleep(1)
    	except:
    		print(f"Input error or you changed mind? please try leter")
    		time.sleep(2)
else: 
	exit()     