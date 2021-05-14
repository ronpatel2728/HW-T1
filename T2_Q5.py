# Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.

if __name__ == '__main__':
    value=[]
    for counter in range(2000,3200+1):
        if (counter%7==0) and (counter%5 !=0):
            value.append(counter)
    print(value)