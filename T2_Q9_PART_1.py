# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.


if __name__ == '__main__':
    guess=10
    while True:
        val_guess=int(input("guess the lucky number : "))
        if guess == val_guess:
            print("Correct guess")
            break

