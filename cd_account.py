# cd_account.py
from Accounts import Account

def create_cd_account(balance, interest_rate, months):
    # Create an instance of the Account class
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100 * months / 12)

    # Update CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Set the balance and interest using the Account class methods
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned
