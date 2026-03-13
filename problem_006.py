def sum_square_difference(n):
    sum_to_n = n/2*(2*1 + (n-1))
    # (a+b+c)^2 = a^2 + b^2 + c^2 + a(b+c) + b(a+c) + c(a+b)
    # a(b+c) + b(a+c) + c(a+b) = a+b+c)^2 - a^2 + b^2 + c^2 + a(b+c)
    diff = 0
    for i in range(1, n+1):
        diff += ((sum_to_n - i) * i)
    return diff

print(sum_square_difference(100))