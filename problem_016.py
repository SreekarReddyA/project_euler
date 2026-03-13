def string_product(str_a, str_b):
    digits_a = [int(d) for d in str_a]
    n = int(str_b)
    digits =[]
    carry = 0
    for d in reversed(digits_a):
        temp = d * n + carry
        digits.insert(0, temp%10)
        carry = temp // 10
    if carry > 0:
        digits.insert(0, carry)
    
    return "".join([str(d) for d in digits])

def power_digit_sum(p):
    
    str_p = '1'
    i = 1
    while i <= p:
        str_p = string_product(str_p, '2')
        i += 1

    int_sum = sum([int(d) for d in str_p])
    return int_sum

print(power_digit_sum(1000))
