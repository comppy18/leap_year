def is_leap_year(year):
    "Returns True if year is leap year"

    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0
