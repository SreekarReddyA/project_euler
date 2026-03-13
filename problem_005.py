def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def smallest_multiple():
    p_list = prime_list(20)
    lcm_dict = {}
    for i in range(1,21):
        p_factors = prime_factors(i, p_list)
        for p in p_factors.keys():
            if p in lcm_dict:
                if lcm_dict[p] < p_factors[p]:
                    lcm_dict[p] = p_factors[p]
            else:
                lcm_dict[p] = p_factors[p]
    lcm = 1
    for l in lcm_dict.keys():
        lcm *= (l**lcm_dict[l])
    return lcm

def prime_list(n):
    prime_list= []
    for i in range(2,n+1):
        is_prime = True
        for p in prime_list:
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    
    return prime_list

def prime_factors(n, prime_list):
    prime_factors = {}
    i = 0
    while i < len(prime_list):
        p = prime_list[i]
        if n % p == 0:
            if p in prime_factors:
                prime_factors[p] += 1
            else:
                prime_factors[p] = 1
            n //= p
        else:
            i += 1
    return prime_factors

print(smallest_multiple())