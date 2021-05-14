# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc


if __name__ == '__main__':

    var = input("Enter the value:")

    if (isinstance(var, float)):
        print("var is float.")
    elif (isinstance(var, int)):
        print("var is integer.")
    elif (isinstance(var, str)):
        print("var is string.")
    else:
        print("Unknow data type")