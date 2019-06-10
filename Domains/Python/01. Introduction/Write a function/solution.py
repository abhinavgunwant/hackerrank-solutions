def is_leap(year):    
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    if year % 100 == 0 and year % 400 == 0:
        return True
    
    return False

year = int(input())
print(is_leap(year))