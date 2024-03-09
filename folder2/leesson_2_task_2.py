def is_year_leap(year):
    if year % 4 == 0:
        print(True)
    else:
        print(False)
        return year
year = int(input("год: "))
result = is_year_leap(year)