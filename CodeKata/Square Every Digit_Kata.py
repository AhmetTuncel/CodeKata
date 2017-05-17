"""
You are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer

"""
def square_digits(num):
    strvl = ""
    for i in str(num):
        strvl += str(int(i)**2)
    return int(strvl)