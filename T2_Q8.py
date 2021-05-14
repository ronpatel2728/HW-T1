# Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.

if __name__ == '__main__':
    var = input("Enter Sample :")
    letter=0
    digits=0
    for va in var:
        if va.isdigit():
            digits = digits + 1
        elif va.isalpha():
            letter = letter + 1
        else:
            pass
    print("Letters "+str(letter)+"    Digits"+str(digits))
