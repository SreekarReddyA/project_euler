# brute force

months_data = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

months_data_leap = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def next_day_of_the_week(day):
    days = {
        'Monday': 'Tuesday',
        'Tuesday': 'Wednesday',
        'Wednesday': 'Thursday',
        'Thursday': 'Friday',
        'Friday': 'Saturday',
        'Saturday': 'Sunday',
        'Sunday': 'Monday',
    }
    return days[day]

def counting_sundays():
    # simulate
    sundays = 0
    day_of_the_month = 1
    month_of_the_year = 1
    year_after_christ = 1900
    day_of_the_week = 'Monday'
    
    while year_after_christ < 2001:
        # print(f"{day_of_the_week}, {day_of_the_month}, {month_of_the_year}, {year_after_christ}")
        if day_of_the_week == 'Sunday' and day_of_the_month == 1 and year_after_christ > 1900:
            sundays += 1
        md = months_data_leap if is_leap(year_after_christ) else months_data
        if day_of_the_month < md[month_of_the_year]:
            day_of_the_month += 1
        else: 
            day_of_the_month = 1
            if month_of_the_year < 12:
                month_of_the_year += 1
            else:
                month_of_the_year = 1
                year_after_christ += 1
        
        day_of_the_week = next_day_of_the_week(day_of_the_week)
    
    return sundays

def is_leap(year_after_christ):
    if year_after_christ % 4 == 0:
        if year_after_christ % 100 == 0:
            if year_after_christ % 400 == 0:
                return True
            return False
        return True
    return False

print(counting_sundays())
