from os import system
import keyboard as ky
def process1():
    print("Process 1")
    a = input("Enter a Character (Process 1): ")
    print(a, "in process 1")

def process2():
    print("Process 2")
    b = input("Enter a Character (Process 2): ")
    print(b, "in process 2")

def redirect():
    system('cls')
    process2()
ky.add_hotkey('ctrl+h', redirect)
process1()
ky.wait()