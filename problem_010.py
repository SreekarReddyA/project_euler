def prime_list(n):
    prime_list= []
    for i in range(2,n+1):
        is_prime = True
        for p in prime_list:
            if p*p > i:
                break
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    
    return prime_list

import math

def summation_of_primes():
    p_list = prime_list(2000000)
    return sum(p_list)

print(summation_of_primes())