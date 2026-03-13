def triangle_numer(n):
    current_number = 0
    tn = 0
    while True:
        current_number += 1
        tn += current_number
        divisors = [1,tn]
        upper_bound = tn
        i = 2
        while i < upper_bound:
            if tn % i == 0:
                divisors.append(i)
                divisors.append(tn//i)
                upper_bound = tn // i
            i += 1
        
        if len(divisors) > n:
            return tn




print(triangle_numer(500))