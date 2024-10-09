# Employee Daily Earnings Calculator

This Python script calculates how much an employee earns on a specific day of a given month, based on a fixed monthly salary. The script takes into account non-working days like **Fridays**, which are automatically excluded from the earnings calculation.

## Features
- Calculates daily earnings for a given day within a month.
- Excludes **Fridays** from working days since they are non-working days.
- Adjusts for different months and years based on user input.
- Allows users to input any year, month, and day for calculation.
- Uses a fixed monthly salary (default: $435) but can be easily modified.

## How the Calculation Works
1. The script asks the user to enter a specific year, month, and day.
2. It calculates the total number of days in that month and determines how many Fridays are present.
3. Fridays are excluded from the total working days, and the daily earnings are computed by dividing the monthly salary by the number of remaining working days.
4. The program then returns the earnings for the specified day, provided it's not a Friday (on Fridays, the earnings are $0).

### Example Calculation:
For **October 2024**:
- October has 31 days, with 4 Fridays.
- There are 27 working days left in October.
- Daily earnings are calculated as $435 / 27 = **$16.11**.

If the user asks for the earnings on a non-Friday, such as October 10th, the earnings will be **$16.11** for that day. If the day is a Friday, the earnings will be **$0**.

## Usage

### Requirements
- **Python 3.x**: The script is written in Python 3, so make sure you have it installed.

### Running the Code
To run the script, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/employee-earnings-calculator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd employee-earnings-calculator
    ```

3. Run the Python script:
    ```bash
    python3 app.py
    ```

4. The program will prompt you to enter the **year**, **month**, and **day**. After inputting the values, the script will calculate the earnings for that specific day.

### Example Run:
```bash
Enter the year (e.g., 2024): 2024
Enter the month (e.g., 10 for October): 10
Enter the day (e.g., 10): 10
The earnings for the employee on 10/10/2024 is: $16.11
