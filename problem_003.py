import math
def largest_prime_factor():
    
    n = 600851475143
    factor = 2
    largest = 0
    while factor*factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        
        factor += 1
    
    return n if n > 1 else largest

print(largest_prime_factor())