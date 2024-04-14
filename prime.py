import math

def is_prime(n: int) -> bool:
    """ Function tests if a number is prime or not
    Parameters:
    n (int) : the number to be checked
    Returns:
    It returns true or false if number is prime or not
    """
    if n <= 1:
        return False  
    # 1 and negative numbers are not prime
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime
    return True  # n is not divisible by any number, so it's prime

def prime_list(numb: int) -> list:
    """ 
    Program gets an integer and returns a list 
    Parameters: 
    numb (int): number asked
    Returns:
    list: returns a list with all the prime numbers up to numb.
    """ 
    lst = []
    for i in range(2, numb + 1):
        if is_prime(i):
            lst.append(i)
    return lst

# Test the prime_list() function
number = int(input("Enter a number to find all prime numbers up to it: "))
prime_numbers = prime_list(number)
print("Prime numbers up to", number, "are:", prime_numbers)
