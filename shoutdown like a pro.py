import os
import time

shutdown = input("Do you wish to shutdown your computer? (yes / no): ").strip().lower()

if shutdown == 'yes':
    info = input("Now? (yes / no): ").strip().lower()
    if info == 'yes':
        print("Shutting down immediately...")
        os.system("shutdown /s /t 1")
        print("Bye Bye")
        time.sleep(1)
    else:
        try:
            info2 = int(input("How many minutes later? ").strip())
            print(f"You will be shut down after {info2} minutes")
            os.system(f"shutdown /s /t {info2 * 60}")
            time.sleep(1)
        except ValueError:
            print("Input error or you changed your mind? Please try again later.")
            time.sleep(2)
else:
    print("Shutdown canceled.")
    exit()