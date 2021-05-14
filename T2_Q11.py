if __name__ == '__main__':
    guess = 10
    counter = 1
    while counter <= 5:
        val_guess = input("guess the lucky number : ")
        if val_guess.isdigit():
            if guess == int(val_guess):
                print("Good guess")
                break
            else:
                print("Try Again")
            counter = counter + 1
