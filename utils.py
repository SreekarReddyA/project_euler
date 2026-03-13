def string_product(str_a, str_b):
    digits_a = [int(d) for d in str_a]
    digits_b = [int(d) for d in str_b]

    # put digit products in a 2-D array
    digit_products = []
    # get the smaller of the two numbers
    is_a_smaller = len(digits_b) > len(digits_a)
    operator = digits_a if is_a_smaller else digits_b
    target = digits_b if is_a_smaller else digits_a

    op_length = len(operator)

    for i in range(len(operator)):
        current_prod_digits = []
        carry = 0
        for _ in range(i):
            current_prod_digits.append('0')
        for j in range(len(target)-1, -1, -1):
            cp = (target[j] * operator[op_length - 1 -i]) + carry
            current_prod_digits.insert(0, str(cp%10))
            carry = cp//10
        if carry > 0:
            current_prod_digits.insert(0, str(carry))
        digit_products.append(current_prod_digits)
    
    product_string = ''
    for d in digit_products:
        product_string = string_sum(product_string, ''.join(d))

    return product_string

def string_sum(str_a, str_b):
    max_len = max(len(str_a), len(str_b))
    str_a = str_a.zfill(max_len)
    str_b = str_b.zfill(max_len)
    dig_a = [int(d) for d in str_a]
    dig_b = [int(d) for d in str_b]
    carry = 0
    sums_array = []
    for i in range(len(dig_a)-1, -1, -1):
        temp_sum = dig_a[i] + dig_b[i] + carry
        sums_array.insert(0, str(temp_sum%10))
        carry = temp_sum // 10
    
    if carry > 0:
        sums_array.insert(0, str(carry))
    
    return ''.join(sums_array)

def get_all_divisors(n):
    divisors = [1]
    upper_bound = n
    i = 2
    while i < upper_bound:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
            upper_bound = n // i
        i += 1
    return divisors