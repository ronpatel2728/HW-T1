#2. Write a program in Python to perform the following operator based task:

# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average


if __name__ == '__main__':
    while True:
        print("Enter 1 - Addition")
        print("Enter 2 - Subtraction")
        print("Enter 3 - Division")
        print("Enter 4 - Multiplication")
        print("Enter 5 - Average")
        varible_op=int(input("Enter operation number : "))
        if varible_op < 6 and  varible_op !=0:
            number1 = int(input("Enter operation number 1 : "))
            number2 = int(input("Enter operation number 2 : "))
            if varible_op ==1:
                value=number2+number1
            elif varible_op ==2:
                value = number1 - number2
            elif varible_op ==3:
                value=number1 / number2
            elif varible_op ==4:
                value = number1 * number2
            elif varible_op ==5:
                value=(number1 + number2)/2
            if value > 0 :
                    print("Operation Value " + str(value))
            else:
                    print("NEGATIVE")
                    break

