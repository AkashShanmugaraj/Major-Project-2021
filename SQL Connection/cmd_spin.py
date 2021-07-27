# This module is used to create a spin effect or loading animation which is certainly cool
# The statement can be customised by providing any string parameter inside the spin function
# This can be used almost anywhere in the program and the only place where it is a problem is the time when the program
# connects to a database.... 
# Currently this test passes

def spin(statement):
    import time
    from datetime import datetime
    symb = ["/","-","\\", "|"]
    symb.extend(symb+symb)
    symb.append("done")
    for i in symb:
        print(statement,i,end = "\r")
        time.sleep(0.25)
    print()
