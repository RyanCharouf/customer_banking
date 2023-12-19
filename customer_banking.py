# customer_banking.py
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Prompt user for savings account details
    savings_balance = float(input("Enter savings account balance: "))
    savings_interest_rate = float(input("Enter savings account interest rate: "))
    savings_months = int(input("Enter number of months for savings account: "))

    # Call create_savings_account function
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print results for savings account
    print(f"\nSavings Account - Interest Earned: {savings_interest_earned}, Updated Balance: {savings_updated_balance}")

    # Prompt user for CD account details
    cd_balance = float(input("\nEnter CD account balance: "))
    cd_interest_rate = float(input("Enter CD account interest rate: "))
    cd_months = int(input("Enter number of months for CD account: "))

    # Call create_cd_account function
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print results for CD account
    print(f"\nCD Account - Interest Earned: {cd_interest_earned}, Updated Balance: {cd_updated_balance}")

# Call the main function
main()
