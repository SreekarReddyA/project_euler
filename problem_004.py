def largest_palindrome():
    # brute force solution
    big_p = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i*j
            if is_palindrome(prod) and prod > big_p:
                big_p = prod
    return big_p

def is_palindrome(n):
    num_string = str(n)
    return num_string == ''.join(list(reversed(num_string)))

print(largest_palindrome())