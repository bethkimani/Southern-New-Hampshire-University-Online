import math

  
#Tpye your code here

# Create variable based on users input
user_num = int(input('Enter integer:\n'))
# Outputs what the user put in
print("You entered:", user_num)

# Squares the users input
user_total = user_num * user_num
# Outputs the squared amount of the users input
print(user_num, "squared is", user_total)

# Cubes the users input
user_cubed = math.pow(user_num, 3)

# Removes the decimal point from the cubed amount
user_num_cubed = math.trunc(user_cubed)
# Outputs the cubed amount of the users input
print("And", user_num, "cubed is", user_num_cubed, "!!")

# Creates a variable from a second user input
user_num2 = int(input('Enter another integer:\n'))
# Outputs the users input
print(user_num2)

# Sums the two user inputs
user_sum = user_num + user_num2
# Outputs the sum of both user inputs
print(user_num, "+", user_num2, "is", user_sum)

# Multiplies the two user inputs
user_prod = user_num * user_num2
# Outputs the product of both user inputs
print(user_num, "*", user_num2, "is", user_prod)
