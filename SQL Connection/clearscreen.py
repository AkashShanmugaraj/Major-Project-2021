# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():
	if name == 'nt':
		_ = system('cls')

# print out some text
print('hello geeks\n'*10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
system('cls')

print("The screen was cleared")

sleep(3)