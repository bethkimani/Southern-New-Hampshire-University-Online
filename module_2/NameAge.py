# Prompt user for name and age, then calculate and display birth year

user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

birth_year = 2025 - user_age

print(f"Hello {user_name}! You were born in {birth_year}.")