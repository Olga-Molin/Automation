def is_year_leap(year):
    if year % 4 == 0:
        return(True)
    else:
        return(False)
    
year = int(input("год: "))
result = is_year_leap(year)
print(result)