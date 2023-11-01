def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True           
    else:
        return False

# TODO: Add more code here
def days_in_month(year, month):
    """Function which return the quantity of days in a month of a certain year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] = 29
    return f"At {year} in the {month} month, have {month_days[month - 1]} days"
        



# ⛔ Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
