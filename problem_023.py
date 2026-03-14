from utils import get_all_divisors
import math
def non_abundant_sums(n):
    abundant_nums = []
    for i in range(1, n+1):
        divisor_sum = sum(list(set(get_all_divisors(i))))
        if divisor_sum > i:
            abundant_nums.append(i)
    
    abundant_nums = sorted(abundant_nums)
    non_ab_sums = []
    all_nums = set(range(1, n+1))
    left = 0

    expressible = set()
    
    while left < len(abundant_nums):
        right = len(abundant_nums) - 1
        while right >= left:
            s = abundant_nums[right] + abundant_nums[left]
            if s in all_nums:
                expressible.add(s)
            right -= 1
        left += 1

    return sum([n for n in all_nums if n not in expressible])

print(non_abundant_sums(28123))

