# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)


if __name__ == '__main__':
    guess=10
    while True:
        val_guess=input("guess the lucky number : ")
        if val_guess.isdigit():
            if guess == int(val_guess):
                print("Correct guess")
                break
        else:
            if val_guess =="no":
                break
            else:
                pass
