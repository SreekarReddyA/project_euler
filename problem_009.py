def special_pythagorean_triplet():
    # max a = 333
    # b = (1000^2 - 2000*a) / (2000 - 2*a)
    for a in range(1,334):
        b = int((1000**2 - 2000*a) / (2000 - 2*a))
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            print(a, b, c)
            return a*b*c
    
    return -1

print(special_pythagorean_triplet())