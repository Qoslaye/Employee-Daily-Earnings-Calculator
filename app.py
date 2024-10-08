import calendar

def calculate_earnings_for_specific_day(year, month, day, monthly_salary):
    """Calculates how much the employee should earn on a specific day"""
    # Check if the day is a Friday
    if calendar.weekday(year, month, day) == 4:  # Friday is represented by 4
        return 0  # No earnings on Fridays
    
    # Get the number of days in the month
    _, days_in_month = calendar.monthrange(year, month)
    
    # Calculate how many Fridays are in the month
    fridays = sum(1 for d in range(1, days_in_month + 1) if calendar.weekday(year, month, d) == 4)
    
    # Calculate the total number of working days (excluding Fridays)
    working_days = days_in_month - fridays
    
    # Calculate the daily earnings
    daily_earnings = monthly_salary / working_days
    
    # Return the earnings for the specific day
    return daily_earnings

# Example usage: interactive input
def main():
    # Ask user for input
    year = int(input("Enter the year (e.g., 2024): "))
    month = int(input("Enter the month (e.g., 10 for October): "))
    day = int(input("Enter the day (e.g., 10): "))
    monthly_salary = 435  # Monthly salary is fixed at $435

    # Calculate the earnings for the specific day
    earnings = calculate_earnings_for_specific_day(year, month, day, monthly_salary)
    
    if earnings == 0:
        print(f"The employee does not earn anything on {day}/{month}/{year} (it's a Friday).")
    else:
        print(f"The earnings for the employee on {day}/{month}/{year} is: ${earnings:.2f}")

# Run the program
main()

