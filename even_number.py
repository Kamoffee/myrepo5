# Implement the function is_even(number) which gets an integer 
# as input parameter and checks, if this input is even or not. is_even() 
# will return the boolean value True if the value is even and False if the input is not even.

# Implement a for loop which iterates over the range(100). 
# Within the for loop, the sequence-variable is checked with the function is_even(). 
# Depending on the return value, either x is even or x is not even is printed.


def is_even(number: int) -> bool:
    """
    Checking if the number is even or not.

    Parameters:
    number (int) : number to be checked.

    Returns:
    bool : True if number is even or False if number is odd.
    """
    return number % 2 == 0

for i in range(100):
    if is_even(i):
        print(i, "is even")
    else:
        print(i, "is not even")