c = int(input("Enter a number: "))

def fac(c):
    if c < 2:
        return 1
    else:
        return c * fac(c - 1)


res = fac(c)
print("Factorial of ", c, " is: ", res)