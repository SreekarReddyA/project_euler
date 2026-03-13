from utils import string_product
def factorial(n):
    if n == 0:
        return '1'
    return string_product(f"{n}", factorial(n-1))

def sum_of_digits(n):
    factorial_string = factorial(n)
    return sum([int(d) for d in factorial_string])

print(sum_of_digits(100))