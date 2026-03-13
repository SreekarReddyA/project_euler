def prime_list(n):
    prime_list= []
    i = 2
    while len(prime_list) < n:
        is_prime = True
        for p in prime_list:
            if p*p > i:
                break
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
        i += 1
    
    return prime_list

def ten_thousand_and_first_prime():
    # brute force
    return prime_list(10001)[-1]

print(ten_thousand_and_first_prime())