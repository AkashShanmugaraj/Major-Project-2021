import time
from datetime import datetime
symb = ["/","-","\\", "|"]
symb.extend(symb+symb)
starttime = datetime.now().time()
username = input("Enter Username: ")
password = input("Enter Password: ")
loopone = 0
for i in symb:
    print("Loading INFO.....",i,end = "\r")
    time.sleep(0.25)

print()
for i in symb:
    print("Retrieving Credentials.....",i,end = "\r")
    time.sleep(0.25)
print()
for i in symb:
    print("Authenticating.....",i,end = "\r")
    time.sleep(0.25)


n = input("\nEnter Name: ")
print(n)