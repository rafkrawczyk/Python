# Initialize variables
monthlyInterestRate = annualInterestRate / 12.0
lower_bound = balance / 12
upper_bound = (balance * (1 + monthlyInterestRate)**12) / 12.0

# Initialize epsilon for precision (how close to 0 do we want to get?)
epsilon = 0.01 

# Start Bisection Search
while True:
    # Guess the midpoint
    guess = (upper_bound + lower_bound) / 2
    
    # Simulate 12 months with this guess
    current_balance = balance
    for month in range(12):
        current_balance -= guess
        current_balance += (monthlyInterestRate * current_balance)
        
    # Check if the balance is close enough to 0
    if abs(current_balance) <= epsilon:
        break
    
    # If balance is positive, we underpaid -> increase lower bound
    elif current_balance > epsilon:
        lower_bound = guess
        
    # If balance is negative, we overpaid -> decrease upper bound
    else:
        upper_bound = guess

# Print result rounded to 2 decimal places
print("Lowest Payment: " + str(round(guess, 2)))