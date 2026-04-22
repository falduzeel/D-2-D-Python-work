def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Rules:
    - Divisible by 4 AND (not divisible by 100 OR divisible by 400)
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Main program
print("=== Leap Year Checker ===")
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a LEAP YEAR! 🐸")
else:
    print(f"{year} is NOT a leap year. 😴")