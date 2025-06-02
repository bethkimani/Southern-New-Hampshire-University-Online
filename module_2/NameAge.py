# NameAge.py
from datetime import datetime

# Get user input
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

# Calculate birth year
current_year = datetime.now().year
birth_year = current_year - user_age

# Display result
print(f"Hello {user_name}! You were born in {birth_year}.")