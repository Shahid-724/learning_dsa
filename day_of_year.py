def get_day(date1):
    # Helper function to check if a year is a leap year
    def isLeapYear(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Helper function to count the days from "1971-01-01" to the given date
    def countDaysFromZero(date):
        year, month, day = map(int, date.split("-"))
        
        # Days per month (non-leap year)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Total days from 1971 to the given year
        days = 0
        for y in range(1, year):
            days += 366 if isLeapYear(y) else 365
        
        # Add days for completed months in the current year
        for m in range(1, month):
            days += days_in_month[m - 1]
            if m == 2 and isLeapYear(year):  # Add 1 day for leap year February
                days += 1
        
        # Add days for the current month
        days += day
        
        return days

    # Calculate the no of days from year 0 to present day
    days = countDaysFromZero(date1)

    # Calculating the day no of the current day
    day = days % 7

    hashmap = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

    return hashmap[day]

date1 = '2025-04-04'
print(get_day(date1))