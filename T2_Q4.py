# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going"

if __name__ == '__main__':

    while True:
        var=int(input("Enter Value : "))
        if var >=0:
            print("Good Going ")
        else:
            print("It’s Over  ")
            break
