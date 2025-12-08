# Example shown for you:
# Create a list of three colors
example_colors = ["red", "blue", "green"]
print("Example:", example_colors)

# Now you try:
# 1. Create a list called 'my_classes' with 4 class names (like "English", "Math", etc.)
my_classes = ["English", "Math", "Science", "History"]
# 2. Create a list called 'my_grades' with 5 test scores (use any numbers between 60-100)
my_grades = [65, 82, 67, 45, 92]
# 3. Create an empty list called 'my_notes'
my_notes = []
# 4. Print all three of your lists

print(my_classes)
print(my_grades)
print(my_notes)

# Lists can hold different types of data!

# 1. Create a list called 'about_me' with:
# - Your first name (string)
# - Your age (integer)
# - Your height in feet (decimal number like 5.5)
# - Whether you like pizza (True or False)
about_me = ["Avery", 19, 5.11, True]

# 2. Create a list called 'mixed_bag' with:
# - The number 42
# - The word "Hello"
# - The value 3.14
# - Another list containing [1, 2, 3]
mixed_bag = [42, "Hello", 3.14, [1, 2, 3]]

# 3. Print both lists
print(about_me)
print(mixed_bag)

# Method 1: Create a list of 10 zeros using multiplication
# Hint: [0] * 10 creates [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

zeros = [0] * 10
# Method 2: Convert a string to a list of characters
# Convert "HELLO" to ['H', 'E', 'L', 'L', 'O']


letters = list("HELLO")
# Method 3: Create a list that repeats [1, 2] three times
# Result should be [1, 2, 1, 2, 1, 2]

pattern = [1, 2] * 3
# Print all three lists
print(zeros)
print(letters)
print(pattern)

# Given this list of months:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Access and print these elements:
print("The list:", months)
print("List length:", len(months))

# 1. Print the first month (remember: first element is at index 0)
print(months[0])

# 2. Print the sixth month (careful with the index!)
print(months[5])

# 3. Print the last month using positive index (hint: use len() - 1)
print(len(months) - 1)

# 4. Print the last month using negative index (hint: -1)
print(months[-1])

# 5. Print December using its positive index
print(months[11])

# 6. Print January using a negative index
print(months[-12])

# 7. Print the month at index 7
print(months[7])


# You're tracking daily temperatures for a week
temperatures = [72, 75, 71, 73, 74, 76, 70] # Sunday through Saturday

print("Original temperatures:", temperatures)

# 1. Monday's temperature was recorded wrong. Change index 1 to 77
temperatures[1] = 77

# 2. Friday's temperature should be 78 (which index is Friday?)
temperatures[5] = 78

# 3. Change Sunday (first day) to 74
temperatures[0] = 74

# 4. Change Saturday (last day) to 72 using negative index
temperatures[6] = 72

# 5. Wednesday (middle of week) should be 75
temperatures[3] = 75

print("Corrected temperatures:", temperatures)

# 6. Calculate and print: how many days are in your list?
print(len(temperatures))

# 7. What's the index of the last day? (print it)
print(temperatures[6])


# Given this small list:
colors = ["red", "blue", "green"]

# 1. Check if index 1 exists before accessing it

if 1 < len(colors):
    print("Color at index 1:", colors[1])
else:
    print("Index 1 doesn't exist")

# 2. Now you try: Check if index 5 exists before trying to access it
if 5 < len(colors):
    print("Color at index 5:", colors[5])
else:
    print("Index 5 doesn't exist")

# 3. Check if the list is empty before accessing the first element
if len(colors) == 0:
    print("The list is empty.")
else:
    print("List is not empty, first element:", colors[0])

# 4. Safely access the last element (check if list has at least 1 item first)
if len(colors) > 0:
    print("Color at index 2:", colors[2])
else:
    print("The list is empty")

# 5. Try to print the element at index -4 (but check if it's valid first)
if -len(colors) <= -4 < len(colors):
    print(colors[-4])
else:
    print("Index out of range.")

# Hint: negative indices from -len(list) to -1 are valid

# 6. What's the smallest valid negative index for this list? Print it.
print(colors[-3])


# Slicing lets us get multiple elements at once!
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Original list:", numbers)
print("Remember: list[start:end] gives elements from start up to (but not including) end")

# Example:
print("Example - numbers[0:3]:", numbers[0:3]) # Gets indices 0, 1, 2

# Now you try:

# 1. Get the first 4 numbers
print("first 4 numbers:", numbers[0: 4])

# 2. Get the last 3 numbers (use negative indices)
print("last 3:", numbers[-3:])

# 3. Get numbers from index 2 to index 6 (30, 40, 50, 60)
print("numbers from index 2 to 6:", numbers[2:6])

# 4. Get all numbers from index 5 to the end
print("numbers from index 5 to end:", numbers[5:])

# 5. Get all numbers from start up to index 4
print("numbers from start to index 4:", numbers[:4])

# 6. Make a complete copy of the list using [:]
copy = numbers[:]
print(copy)

# 7. Get an empty slice (like numbers[3:3]) and see what happens
print(numbers[4:4])


# We can use a step value: list[start:end:step]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

print("Alphabet:", alphabet)

# Example:
print("Every other letter:", alphabet[::2]) # Start to end, step by 2

# Now you try:

# 1. Get every third letter starting from 'a' (indices 0, 3, 6, 9, 12)
print("every third letter:",alphabet[0::3])

# 2. Get every other letter starting from 'b' (indices 1, 3, 5, 7, ...)
print("every letter starting from 'b':",alphabet[1::3])

# 3. Reverse the entire list using slicing (hint: use step of -1)
print("reverse:",alphabet[::-1])

# 4. Get the first half of the alphabet
print("first half:",alphabet[:6])

# Hint: Calculate middle index using len() // 2

# 5. Get the second half of the alphabet
print("second half:",alphabet[6:])

# 6. Get letters from index 2 to 8, but only every other one
print("letters from index 2 to 8:", alphabet[2:8])

# 7. Reverse just the first 5 letters (get them, then reverse)
print("reverse first 5:", alphabet[:5][::-1])


# You have hourly temperature readings for a day (24 hours)

hourly_temps = [55, 54, 53, 52, 52, 54, 58, 62, 66, 70, 73, 75, 76, 77, 77, 76, 74, 71, 68, 65, 62, 59, 57, 55]
print(f"24-hour temperature data ({len(hourly_temps)} readings)")

# 1. Get morning temperatures (first 6 hours, 12am-5am)
print("morning temperatures:", hourly_temps[:6])

# 2. Get afternoon temperatures (12pm-5pm, which is indices 12-17)
print("afternoon temperatures:", hourly_temps[12:17])

# 3. Get evening temperatures (last 6 hours, 6pm-11pm)
print("evening temperatures:", hourly_temps[18:])

# 4. Get every other hour's temperature for the whole day
print("every other hour's temperature:", hourly_temps[::2])

# 5. Get the middle 4 hours of the day (hours 10-13, so indices 10-14)
print("middle 4 temperatures:", hourly_temps[10:14])

# 6. What were the temperatures for hours 6-9am? (indices 6-9)
print("temps from 6 to 9 AM:", hourly_temps[6:9])


# append() adds ONE item to the end of a list
shopping_list = []
print("Starting with empty list:", shopping_list)
# Add these items one at a time using append():

# 1. Add "milk"
shopping_list.append("milk")

# 2. Add "bread"
shopping_list.append("bread")

# 3. Add "eggs"
shopping_list.append("eggs")

# 4. Add "cheese"
shopping_list.append("cheese")

# 5. Add "apples"
shopping_list.append("apples")

print("Final shopping list:", shopping_list)

# 6. What happens if you try to append two items at once?

# Try: shopping_list.append("butter", "yogurt") # can only append one item
# Comment out the line after you see the error!

# 7. Create a list with your 3 favorite foods using append()

favorites = []
favorites.append("cocolate milk")
favorites.append("cheese")
favorites.append("apples")

# Add your three favorites here
print("My favorites:", favorites)


# insert() adds an item at a specific position
line = ["Alice", "Bob", "Charlie"]
print("Original line:", line)

# 1. David cuts to the front! Insert "David" at index 0
print("After David cuts:", line.insert(0, "David"))

# 2. Eve joins between Alice and Bob (what index?)
print("After Eve joins:", line.insert(2, "Eve"))

# 3. Frank joins at the end (what index? Use len())
print("Final line:", line)


# Now create a schedule:
schedule = ["Math", "History", "Science"]
print("\nOriginal schedule:", schedule)

# 4. Add "Lunch" between History and Science
schedule.insert(2, "Lunch")

# 5. Add "Homeroom" at the beginning
schedule.insert(0, "Homeroom")

print("Updated schedule:", schedule)


# extend() adds ALL items from another list
primary_colors = ["red", "blue", "yellow"]
print("Primary colors:", primary_colors)

# 1. Create a list of secondary colors
secondary_colors = ["green", "orange", "purple"]

# 2. Add all secondary colors to primary_colors using extend()
print("All colors:", primary_colors.extend(secondary_colors))

# Compare append vs extend:
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# 3. Append [4, 5] to list1 (this adds the list as one item!)
list1.append([4, 5])
print("After append([4, 5]):", list1)

# 4. Extend list2 with [4, 5] (this adds each item separately)
list2.extend([4, 5])
print("After extend([4, 5]):", list2)

# 5. Create your own example showing the difference
my_list = ["a", "b"]

# Try both append and extend with ["c", "d"] and print results
print(my_list)
my_list.append(["c", "d"])
my_list.extend(["c", "d"])
print(my_list)


# remove() deletes the FIRST occurrence of a value
pets = ["dog", "cat", "bird", "cat", "fish", "cat"]
print("Original pets:", pets)

# 1. Remove "bird"
print("After removing bird:", pets.remove("bird"))

# 2. Remove "cat" (notice it only removes the first one!)
print("After removing one cat:", pets.remove("cat"))

# 3. Check if "hamster" is in the list before trying to remove it
if "hamster" in pets:
    pets.remove("hamster")
else:
    print("hamster not found in list")

# 4. Create a list with duplicate values
numbers = [5, 3, 8, 3, 9, 3, 2]
dup = numbers * 3
print("\nNumbers:", dup)

# 5. Remove all 3's (one at a time, checking each time)
while 3 in numbers:
    if 3 in numbers:
        numbers.remove(3)
        print("Removed first 3:", numbers)

# Remove the remaining 3's (you'll need more if statements)


# pop() removes AND RETURNS an item by index
stack = [10, 20, 30, 40, 50]
print("Original stack:", stack)

# 1. Remove and save the last item
last_item = stack.pop()
print(f"Popped {last_item}, stack is now: {stack}")

# 2. Remove and save the first item (index 0)
stack.pop(0)
print("Current stack:", stack)

# 3. Remove the item at index 1
stack.pop(1)
print("Current stack:", stack)

# Working with a queue:
queue = ["Person1", "Person2", "Person3", "Person4"]
print("\nQueue:", queue)

# 4. Serve (remove) the first person in line and print who was served
queue.pop(0)

# 5. The last person gives up and leaves (remove but don't save)
print("Remaining queue:", queue)


# del can remove items by index or slice
data = [100, 200, 300, 400, 500, 600, 700]
print("Original data:", data)

# 1. Delete the first element using del
del data[0]
print("After deleting first:", data)

# 2. Delete the element at index 2
del data[2]
print("After deleting index 2:", data)

# 3. Delete a slice from index 1 to 3 (not including 3)
del data[1:3]
print("After deleting slice:", data)

# Working with unwanted data:
readings = [0, 5, -999, 10, 15, -999, 20] # -999 represents bad data
print("\nReadings with errors:", readings)

# 4. Find and remove the first -999 using remove()
while -999 in readings:
    if -999 in readings:
        readings.remove(-999)
        print(readings)

# 5. Check if there are more -999 values and remove them
print("Clean readings:", readings)


# Check if items are in a list
valid_grades = ['A', 'B', 'C', 'D', 'F']
print("Valid grades:", valid_grades)

# 1. Check if 'B' is a valid grade
if 'B' in valid_grades:
    print("B is a valid grade")

# 2. Check if 'E' is NOT a valid grade
if 'E' not in valid_grades:
    print("E is not a valid grade")

# 3. Ask user for a grade and check if it's valid
grade_input = input("Enter in a letter grade: ")
while grade_input not in valid_grades:
    if grade_input in valid_grades:
        print(f"{grade_input} is a valid grade.")
    else:
        print("please enter a valid grade")
        grade_input = input("Enter in a letter grade: ")

user_grade = 'C' # Pretend user entered this
# Check if user_grade is in valid_grades
# Working with a menu:
menu_options = [1, 2, 3, 4, 5]
print("\nMenu options:", menu_options)

# 4. Check if option 3 is available
if 3 in menu_options:
    print(f"menu option {menu_options[2]} is avaliable")
else:
    print(f"menu option {menu_options[2]} is not avaliable")

# 5. Check if option 9 is NOT available
if 9 in menu_options:
    print(f"menu option 9 is avaliable")
else:
    print(f"menu option 9 is not avaliable")

# Student roster:
enrolled = ["Alice", "Bob", "Charlie", "Diana"]
print("\nEnrolled students:", enrolled)

# 6. Check if "Eve" needs to be added (not in list)
if "Eve" not in enrolled:
    enrolled.append("Eve")

# 7. Only add "Frank" if not already enrolled
if "Frank" not in enrolled:
    enrolled.append("Frank")
print("\nEnrolled students updated:", enrolled)

# 8. Create a list of students to check
to_check = ["Alice", "Eve", "Bob", "George"]
print("\nStudents to check:", to_check)

if to_check[0] in enrolled:
    print(f"{to_check[0]} is enrolled.")
else:
    print(f"{to_check[0]} is NOT enrolled.")

if to_check[1] in enrolled:
    print(f"{to_check[1]} is enrolled.")
else:
    print(f"{to_check[1]} is NOT enrolled.")

if to_check[2] in enrolled:
    print(f"{to_check[2]} is enrolled.")
else:
    print(f"{to_check[2]} is NOT enrolled.")

if to_check[3] in enrolled:
    print(f"{to_check[3]} is enrolled.")
else:
    print(f"{to_check[3]} is NOT enrolled.")

# For each student, print whether they're enrolled or not
# (Do this without loops - check each one individually)


# len() tells us how many items are in a list
tasks = ["homework", "dishes", "laundry", "shopping", "exercise"]
print("Tasks:", tasks)

# 1. How many tasks are there?
print(len(tasks))

# 2. What's the index of the last task? (remember: len() - 1)
print(len(tasks) - 1)

# 3. Check if list has more than 3 tasks
if len(tasks) > 3:
    print("There are more than 3 tasks.")
else:
    print("There are not more than 3 tasks.")

# 4. Calculate the middle index
print(len(tasks) / 2)

# 5. Access the middle task safely
print(tasks[2])

# Empty list checks:
inbox = []
print("\nInbox:", inbox)

# 6. Check if inbox is empty (two ways)
if len(inbox) < 1:
    print("Inbox is empty (using len() < 1)")

# Way 1: Check if len() == 0
if len(inbox) == 0:
    print("Inbox is empty (using len() == 0)")

# Way 2: Empty lists are "falsy"
if (bool(inbox) == False):
    print("Inbox is empty (using 'falsy')")

if not inbox:
    print("Inbox is empty (using 'not inbox')")

# 7. Create a waiting list with max capacity of 4
waiting = ["P1", "P2"]
max_capacity = 4
print(f"\nWaiting list ({len(waiting)}/{max_capacity}):", waiting)

# How many more can join?
spaces_available = max_capacity - len(waiting)
print(f"Spaces available: {spaces_available}")

# Add two more if there's room
if len(waiting) < max_capacity:
    waiting.append("P3")
if len(waiting) < max_capacity:
    waiting.append("P4")
print(f"Updated waiting list ({len(waiting)}/{max_capacity}):", waiting)