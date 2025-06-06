# Defining the function 
def exact_change(user_total):
    if user_total <= 0:  # Handle 0 or negative input
        return 0, 0, 0, 0, 0
    
    num_dollars = user_total // 100
    remaining = user_total % 100  # Use remaining amount for next calculation
    num_quarters = remaining // 25  # Fixed: Use remaining, not num_dollars
    remaining = remaining % 25  # Update remaining after quarters
    num_dimes = remaining // 10  # Fixed: Use remaining, not num_quarters
    remaining = remaining % 10  # Update remaining after dimes
    num_nickels = remaining // 5  # Fixed: Use remaining, not num_dimes
    remaining = remaining % 5  # Update remaining after nickels
    num_pennies = remaining  # Fixed: Pennies are the remaining amount
    
    return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)  # Fixed: Return correct counts

if __name__ == '__main__':  # Fixed typo: _name_ to __name__, _main_ to __main__
    while True:  # Loop until valid input is received
        try:
            input_val = int(input("Enter the total change amount in cents: "))  # Prompt user
            num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if input_val <= 0:  # Fixed: Handle 0 or negative input
        print('no change')
    else:  # Only print non-zero counts
        if num_dollars == 1:
            print(num_dollars, 'dollar')
        elif num_dollars > 1:  # Fixed: Use > 1 to skip 0
            print(num_dollars, 'dollars')
        if num_quarters == 1:
            print(num_quarters, 'quarter')
        elif num_quarters > 1:  # Fixed: Use > 1 to skip 0
            print(num_quarters, 'quarters')
        if num_dimes == 1:
            print(num_dimes, 'dime')
        elif num_dimes > 1:  # Fixed: Use > 1 to skip 0
            print(num_dimes, 'dimes')
        if num_nickels == 1:
            print(num_nickels, 'nickel')
        elif num_nickels > 1:  # Fixed: Use > 1 to skip 0
            print(num_nickels, 'nickels')
        if num_pennies == 1:
            print(num_pennies, 'penny')
        elif num_pennies > 1:  # Fixed: Use > 1 to skip 0
            print(num_pennies, 'pennies')