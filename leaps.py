def check_year(year):
    # Returns True if leap year, else False
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def next_leap_year(year):
    print(f"Checking year = {year + 1}")   
    year += 1

    if check_year(year):
        print(f"{year} is a leap year ")
        return year
    else:
        return next_leap_year(year)        # recursive call



y = int(input("Enter the year: "))
print("The next leap year:", next_leap_year(y))
