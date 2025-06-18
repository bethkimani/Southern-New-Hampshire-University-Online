# Prompt user for input and get the total change amount in cents
money = int(input("Enter the total change amount in cents: "))

if money <= 0:
    print('No change')

# Variables to hold the number of each coin
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# Calculate dollars
dollars = money // 100
if dollars > 0:
    money = money - (dollars * 100)
    if dollars == 1:
        print(dollars, 'Dollar')
    elif dollars > 1:
        print(dollars, 'Dollars')

# Calculate quarters
quarters = money // 25
if quarters > 0:
    money = money - (quarters * 25)
    if quarters == 1:
        print(quarters, 'Quarter')
    elif quarters > 1:
        print(quarters, 'Quarters')

# Calculate dimes
dimes = money // 10
if dimes > 0:
    money = money - (dimes * 10)
    if dimes == 1:
        print(dimes, 'Dime')
    elif dimes > 1:
        print(dimes, 'Dimes')

# Calculate nickels
nickels = money // 5
if nickels > 0:
    money = money - (nickels * 5)
    if nickels == 1:
        print(nickels, 'Nickel')
    elif nickels > 1:
        print(nickels, 'Nickels')

# Calculate pennies
pennies = money // 1
if pennies > 0:
    if pennies == 1:
        print(pennies, 'Penny')
    elif pennies > 1:
        print(pennies, 'Pennies')