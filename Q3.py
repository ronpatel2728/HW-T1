#Swap two numbers using a third variable and do the same task without using any third variable
##created function for with using third varible
def with_out(a,b):
    a=a
    b=b
    b,a=a,b
    print("value of a ",a)
    print("value of b ",b)

def using_third(a,b):
    a=a
    b=b
    c=a
    a=b
    b=c
    print("value of a",a)
    print("value of b",b)
if __name__ == '__main__':
    ## index first for a, second index is for b
    with_out(15,17)
    ## index first for a, second index is for b
    using_third(21,22)

