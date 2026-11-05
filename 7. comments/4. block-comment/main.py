# Customer account information
account_number = "123456789"
account_holder = "John Doe"
balance = 1000.50

# Process withdrawal
withdrawal_amount = 200.00
if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f"Withdrawal of ${withdrawal_amount} successful.")
else:
    print("Insufficient funds for withdrawal.")

# Display updated account information
print(f"Account Number: {account_number}")
print(f"Account Holder: {account_holder}")
print(f"Updated Balance: ${balance:.2f}")