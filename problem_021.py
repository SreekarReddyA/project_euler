from utils import get_all_divisors

def amicable_number(n):
    nums = list(range(1, n))
    amicable_nums = nums.copy()
    for i in nums:
        if not i in amicable_nums: 
            continue
        sum_divisors_i = sum(get_all_divisors(i))
        if sum_divisors_i == 1: # we have a prime number
            ind_i = amicable_nums.index(i)
            amicable_nums[ind_i] = 0
            continue
        div_sum_j = sum(get_all_divisors(sum_divisors_i))
        if div_sum_j != i or div_sum_j == sum_divisors_i:
            ind_i = amicable_nums.index(i)
            amicable_nums[ind_i] = 0
    return sum(amicable_nums)

print(amicable_number(10000))