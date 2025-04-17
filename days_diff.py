def calculateDifference(self, date1: str, date2: str):
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
        for y in range(0, year):
            days += 366 if isLeapYear(y) else 365
        
        # Add days for completed months in the current year
        for m in range(1, month):
            days += days_in_month[m - 1]
            if m == 2 and isLeapYear(year):  # Add 1 day for leap year February
                days += 1
        
        # Add days for the current month
        days += day
        
        return days

    # Calculate days for both dates
    days1 = countDaysFromZero(date1)
    days2 = countDaysFromZero(date2)

    # Calculate absolute difference in days
    days_difference = abs(days2 - days1)
    
    # Calculate weeks, months, and years
    weeks_difference = days_difference // 7
    months_difference = days_difference // 30  # Approximate months (30 days per month)
    years_difference = days_difference // 365  # Approximate years (365 days per year)
    
    return {
        "days": days_difference,
        "weeks": weeks_difference,
        "months": months_difference,
        "years": years_difference
    }