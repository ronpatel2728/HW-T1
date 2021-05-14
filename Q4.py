#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.

import sys


if __name__ == '__main__':
    user_input=input("Enter User input")
    if sys.version_info <( 2,9):
        print ("Enter values using 2.x", user_input)
    else :
        print(" Entered values using print 3.x",user_input)