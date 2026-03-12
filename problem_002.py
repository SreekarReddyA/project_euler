def even_fibonacci_sum():
    f_sum = 0
    fib_number_old = 0
    fib_number = 1
    while fib_number < 4000000:
        f_sum += fib_number if fib_number%2 == 0 else 0
        temp = fib_number
        fib_number =  fib_number + fib_number_old
        fib_number_old = temp

    return f_sum

even_fibonacci_sum()