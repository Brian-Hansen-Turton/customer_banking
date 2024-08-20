# Account Interest Calculator

This Python script calculates the interest earned and updates the balances for both a savings account and a Certificate of Deposit (CD) account. The user is prompted to enter their account balances, interest rates, and the duration (in months) to calculate the total interest earned and the new balance.

## Features

- **Savings Account Interest Calculation:** The script calculates the interest earned on a savings account based on the user-provided balance, interest rate, and maturity period in months.
- **CD Account Interest Calculation:** Similar to the savings account, the script also calculates the interest earned on a CD account over a specified number of months.
- **Balance Updates:** After calculating the interest, the script updates the balances for both the savings and CD accounts and displays the new balances along with the interest earned.

## How It Works

1. **Input Prompts:**
   - The user is prompted to enter the initial balance, annual interest rate, and the maturity period (in months) for both the savings and CD accounts.

2. **Interest Calculation:**
   - The script uses the `create_savings_account` function to calculate the interest and new balance for the savings account.
   - It then uses the `create_cd_account` function to do the same for the CD account.

3. **Output:**
   - The script displays the interest earned and the updated balance for each account.

## Usage

### Running the Script

1. **Import the Required Functions:**
   - Ensure that the functions `create_savings_account` and `create_cd_account` are properly imported from their respective modules:
     ```python
     from cd_account import create_cd_account
     from savings_account import create_savings_account
     ```

2. **Execute the Script:**
   - Run the script in a Python environment. It will prompt you for input values.

3. **Input the Following Values:**
   - Savings account balance.
   - Savings account annual interest rate.
   - Savings account maturity period in months.
   - CD account balance.
   - CD account annual interest rate.
   - CD account maturity period in months.

4. **Review the Output:**
   - The script will output the updated balances and the interest earned for both the savings and CD accounts.

### Example

```plaintext
Please enter your savings account balance. 1000
Please enter your savings account interest rate. 5
Please enter your savings maturity 12
Your new balance is $1,051.16 and your interest was $51.16


Please enter your CD account balance. 5000
Please enter your CD account interest rate. 3
Please enter your CD accounts maturity 24
You earned $306.16 in interest and your new CD account balance is $5,306.16
