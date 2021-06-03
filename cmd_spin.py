def spin(statement):
    import time
    from datetime import datetime
    symb = ["/","-","\\", "|"]
    symb.extend(symb+symb)
    symb.append("done!")
    starttime = datetime.now().time()
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    loopone = 0
    for i in symb:
        print(statement,i,end = "\r")
        time.sleep(0.25)

    n = input("\nEnter Name: ")
    print(n)
spin("Thinking.....")
time.sleep(10)
