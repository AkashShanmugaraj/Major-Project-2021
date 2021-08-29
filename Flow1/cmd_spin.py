# This module is used to create a spin effect or loading animation which is certainly cool
# The statement can be customised by providing any string parameter inside the spin function

def spin(statement):
    import time
    symb = ["/","-","\\", "|"]
    symb.extend(symb)
    symb.append("done")
    for i in symb:
        print(statement,i,end = "\r")
        time.sleep(0.25)
    print()
