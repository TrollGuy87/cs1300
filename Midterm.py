"""
Problem 1: String Processing
Complete each task below.
"""

# Given information (DO NOT MODIFY):
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

# Task 1.1 (3 points): Extract and print the first name only
firstName = full_name[0:4]
print(firstName)

# Task 1.2 (3 points): Extract and print the last name only
lastName = full_name[13:18]
print(lastName)

# Task 1.3 (3 points): Create and print initials (J.M.S.)
Initials = "J.M.S"
print(Initials)

# Task 1.4 (3 points): Check if the email contains "university" (case-insensitive)
if ("university" in email) == True:
    print("University is in email")

# Task 1.5 (3 points): Replace all dashes in phone with spaces and print
phone = "555 123 4567"
print(phone)

"""
Problem 2: Restaurant Rating Calculator
Calculate based on percentage rating.
"""

# Task 2.1 (3 points): Get these ratings
atmosphere = 4.5
food = 3.4
service = 2.5
cleanness = 3.0

# Task 2.2 (4 points): Calculate weighted average
atmosphere * 0.1
food * 0.45
service * 0.2
cleanness * 0.25

# Weights: atmosphere=10%, food=45%, service=20%, cleanness=25%

# Store result in variable 'average'
average = []
average.extend([atmosphere, food, service, cleanness])

# Task 2.3 (8 points): Determine restaurant rating

# Use these ranges:
stars = ""

for item in average:
# *****: 4.0 and above
    if item >= 4.0:
        stars = "*****"
        print(item, stars)
# ****: 3.0-4.0
    elif item >= 3.0:
        stars = "****"
        print(item, stars)
# ***: 2.0-3.0
    elif item >= 2.0:
        stars = "***"
        print(item, stars)
# **: 1.0-2.0
    elif item >= 1.0:
        stars = "**"
        print(item, stars)
# *: below 1.0
    elif item < 1.0:
        stars = "*"
        print(item, stars)

# Print both the average and star rating

"""
Problem 3: Movie Review Number Management
Manage a list of movie review numbers.
"""

# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]
print(numbers)

# Task 3.2 (3 points): Add a new review number of 4 to the end
numbers.append(4)
print(numbers)

# Task 3.3 (3 points): The third review number (4) was entered wrong.
# Change it to 3
numbers[2] = 3
print(numbers)

# Task 3.4 (3 points): Remove the review number 1 from the list
numbers.remove(3)
print(numbers)

# Task 3.5 (3 points): Insert a review number of 3 at position 2
numbers.insert(2, 3)
print(numbers)

# Task 3.6 (3 points): Create and print a sublist of the first 3 numbers
firstThree = numbers[0:3]
print(firstThree)

# Task 3.7 (3 points): Print:

# - How many movie review numbers

print("This is how many numbers are in the list:", len(numbers))

# - The first review number
print(numbers[0])

# - The last review number
print(numbers[7])

"""
Problem 4: Shopping Cart System
Build a basic shopping cart with price checking.
"""

# Initial setup (DO NOT MODIFY):
items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99] # Matching prices for each item
cart = []
cart_total = 0.0


# Task 4.1 (4 points): Add "milk" to cart
# Check if "milk" is in items, find its index, and add to cart
if ("milk" in items) == True:
    print("milk is in items")
    cart.extend([items[1], prices[1]])
# Also add its price to cart_total
print(cart)

# Task 4.2 (4 points): Add "eggs" to cart
if ("eggs" in items) == True:
    cart.extend([items[2], prices[2]])
print(cart)

# Same process as above

# Task 4.3 (4 points): Try to add "cookies" to cart
if ("cookies" in items) == True:
    print("cookies are in items")
else:
    print("cookies are not in items")

# Check if it exists first, print appropriate message

# Task 4.4 (4 points): Apply discount
cart_total = cart[1] + cart[3]
print("since price is above 6 dollars you get a 10% discount!   ")

# If cart_total > 6.00, apply 10% discount
discounted_total = (cart_total / 100) * 10

# Print the original total and discounted total

# Task 4.5 (4 points): Final report

# Print:

# - Items in cart
print(cart)

# - Number of items
print("number of items is 2")

# - Final total (with discount if applicable)
print("original total: $", cart_total)
print(f"discount total: $ {discounted_total:.2f}")