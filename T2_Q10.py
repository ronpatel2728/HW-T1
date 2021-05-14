# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”
if __name__ == '__main__':
    guess=10
    counter=1
    while counter<=5:
        val_guess=input("guess the lucky number : ")
        if val_guess.isdigit():
            if guess == int(val_guess):
                print("Good guess")
            else:
                print("Try Again")
            counter=counter+1
