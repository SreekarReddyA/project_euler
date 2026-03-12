import math
def multiple_sum():
    m_sum = 0
    for i in range(1001):
        m_sum += i if i%3 == 0 or i%5 == 0 else 0
    
    return m_sum

# print(multiple_sum())

def multiple_sum_ap_formula():
    number_of_multiples_of_three = math.floor(1000/3)
    number_of_multiples_of_five = math.floor(1000/5)
    number_of_multiples_of_fifteen = math.floor(1000/15)
    ap_sum_three = number_of_multiples_of_three/2 * (2*3 + (number_of_multiples_of_three - 1) * 3)
    ap_sum_five = number_of_multiples_of_five/2 * (2*5 + (number_of_multiples_of_five - 1) * 5)
    ap_sum_15 = number_of_multiples_of_fifteen/2 * (2*15 + (number_of_multiples_of_fifteen - 1) * 15)
    return ap_sum_three + ap_sum_five - ap_sum_15

print(multiple_sum_ap_formula())