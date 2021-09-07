# cmd_spin.py
def spin(statement):
    import time
    symb = ["/","-","\\", "|"]
    symb.extend(symb)
    symb.append("done")
    for i in symb:
        print(statement,i,end = "\r")
        time.sleep(0.25)
    print()
