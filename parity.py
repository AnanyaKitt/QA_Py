"""
# Is the number can dived by ...
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""


# If create as a def
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
