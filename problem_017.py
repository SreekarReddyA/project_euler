def deal_with_tens(i):
    string = ""
    if i == 2:
        string += "twenty"
    elif i == 3:
        string += "thirty"
    elif i == 4:
        string += "forty"
    elif i == 5:
        string += "fifty"
    elif i == 6:
        string += "sixty"
    elif i == 7:
        string += "seventy"
    elif i == 8:
        string += "eighty"
    elif i == 9:
        string += "ninety"
    return string

def deal_with_units(i_mod_ten):
    string = ""
    if i_mod_ten == 1:
        string += "one"
    elif i_mod_ten == 2:
        string += "two"
    elif i_mod_ten == 3:
        string += "three"
    elif i_mod_ten == 4:
        string += "four"
    elif i_mod_ten == 5:
        string += "five"
    elif i_mod_ten == 6:
        string += "six"
    elif i_mod_ten == 7:
        string += "seven"
    elif i_mod_ten == 8:
        string += "eight"
    elif i_mod_ten == 9:
        string += "nine"
    return string

def deal_with_teens(i_mod_hundered):
    string = ""
    if i_mod_hundered == 10:
        string += "ten"
    elif i_mod_hundered == 11:
        string += "eleven"
    elif i_mod_hundered == 12:
        string += "twelve"
    elif i_mod_hundered == 13:
        string += "thirteen"
    elif i_mod_hundered == 14:
        string += "fourteen"
    elif i_mod_hundered == 15:
        string += "fifteen"
    elif i_mod_hundered == 16:
        string += "sixteen"
    elif i_mod_hundered == 17:
        string += "seventeen"
    elif i_mod_hundered == 18:
        string += "eighteen"
    elif i_mod_hundered == 19:
        string += "nineteen"
    return string
        

def get_char_count_teens(n):
    count = 0
    for i in range(1, n+1):
        if i > 9:
            count += len(deal_with_units(i))
        else:
            count += len(deal_with_teens(i))
    return count

# brute force
def number_letter_counts(n):
    strings = []
    for i in range(1, n+1):
        num_string = ""
        i_mod_10 = i%10
        i_mod_100 = i%100

        i_divisor_100 = i//100
        i_divisor_1000 = i//1000

        if i_divisor_1000 == 1: # dealing with exactly thousand
            num_string += deal_with_units(i_divisor_1000)
            num_string += "thousand"
        elif i_divisor_100 > 0: #dealing with a number greater than 100
            num_string += deal_with_units(i_divisor_100)
            num_string += "hundred"
            if i_mod_100 > 0: #number is not an exact hundered
                num_string += "and"
        if i_mod_100 >= 20: # last two digits are greater than 20
            num_string += deal_with_tens(i_mod_100//10)
            num_string += deal_with_units(i_mod_10)
        elif i_mod_100 >= 10:
            num_string += deal_with_teens(i_mod_100)
        else:
            num_string += deal_with_units(i_mod_10)
        
        strings.append(num_string)
    
    return sum([len(s) for s in strings])

print(number_letter_counts(1000))