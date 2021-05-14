# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statemen


if __name__ == '__main__':
    for rang in range(0,6+1):
            if rang !=3 and rang !=6:
                    print(rang,end=" ")
                    continue
