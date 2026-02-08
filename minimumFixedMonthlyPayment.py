#Example Variables
#balance = 4773
#annualInterestRate = 0.2

# Initialize starting guess
monthlyPayment = 0
currentBalance = balance

# Monthly interest rate is constant
monthlyInterestRate = annualInterestRate / 12.0

# Keep trying until the balance is paid off
while currentBalance > 0:
    # Increase the payment guess by $10
    monthlyPayment += 10
    
    # Reset the balance to the original amount for a fresh simulation
    currentBalance = balance
    
    # Simulate 12 months
    for month in range(12):
        # Apply payment
        currentBalance -= monthlyPayment
        
        # Add interest to the remaining balance
        currentBalance += (monthlyInterestRate * currentBalance)

# Once the loop exits, we found the lowest payment that works
print("Lowest Payment: " + str(monthlyPayment))