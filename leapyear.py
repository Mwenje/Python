def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        return print(f"{year} is a leap year")
    else:
        return print(f"{year} is not year")


is_leap_year(2000)
