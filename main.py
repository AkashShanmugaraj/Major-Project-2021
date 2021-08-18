import pyfiglet
from os import system
def home():
    print(pyfiglet.figlet_format("Welcome Akash Shanmugaraj", font = "digital" ))
    menu = '''Do you want to \n\t1. add a book?\n\t2. edit a book? \n\t3. create a new transaction\n\t4.view transactions?\n\t5.view books?\n\t7. Exit App\n...... '''
    q = int(input(menu))
    if q == 1:
        system('clear')

    elif q == 2:
        system('clear')
    elif q == 3:
        system('clear')
    elif q == 4:
        system('clear')
    elif q == 5:
        system('clear')
    elif q == 7:
        exit()
home()