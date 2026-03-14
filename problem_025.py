from utils import string_sum
def big_fibonacci_number(n):
    index = 2
    f_n_2 = '1'
    f_n_1 = '1'
    while True:
        index += 1
        temp = f_n_1
        f_n_1 = string_sum(f_n_1, f_n_2)
        f_n_2 = temp
        print
        if len(f_n_1) == n:
            return index

print(big_fibonacci_number(1000))