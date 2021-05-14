# Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.


if __name__ == '__main__':
    while True:
        value_1=int(input("Enter value for varible 1"))
        if value_1<=10:
            value_2=int(input("Enter value for varible 2"))
            if value_2 <=10:
                z=value_1+value_2
                result=z+30
                print(result)
                break
            else:
                print(" value required in between 1 to 10 for varible2")
        else:
                print(" value required in between 1 to 10 for varible 1")

