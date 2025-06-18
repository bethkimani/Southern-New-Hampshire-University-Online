# Defining the function 
def exact_change(user_total):
    if user_total <= 0:
        return 0, 0, 0, 0, 0
    
    num_dollars = user_total // 100
    remaining = user_total % 100
    num_quarters = remaining // 25
    remaining = remaining % 25
    num_dimes = remaining // 10
    remaining = remaining % 10
    num_nickels = remaining // 5
    remaining = remaining % 5
    num_pennies = remaining
    
    return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)

if __name__ == '__main__':
    while True:
        try:
            input_val = int(input())  
            num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid integer")

    if input_val <= 0:
        print("no change")
    else:
        if num_dollars == 1:
            print(num_dollars, 'dollar')
        elif num_dollars > 1:
            print(num_dollars, 'dollars')
        if num_quarters == 1:
            print(num_quarters, 'quarter')
        elif num_quarters > 1:
            print(num_quarters, 'quarters')
        if num_dimes == 1:
            print(num_dimes, 'dime')
        elif num_dimes > 1:
            print(num_dimes, 'dimes')
        if num_nickels == 1:
            print(num_nickels, 'nickel')
        elif num_nickels > 1:
            print(num_nickels, 'nickels')
        if num_pennies == 1:
            print(num_pennies, 'penny')
        elif num_pennies > 1:
            print(num_pennies, 'pennies')