"""
#### Problem 1 ####

print("=== Temperature Converter & Weather Advisor ===")

# Get temperature from user
temp = float(input("Enter temperature: "))

# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()

if scale == "C":
    print(f"{temp}°C = {(temp * (9/5)) + 32}°F")
elif scale == "F":
    print(f"{temp}°F = {(temp - 32) * 5/9}°C")

if temp < 32:
    print("Freezing! Bundle up warmly!")
elif temp <= 50:
    print("Cold - wear a warm jacket")
elif temp <= 70:
    print("Warm - enjoy the weather!")
elif temp <= 85:
    print("Hot - stay hydrated")
elif temp > 85:
    print("HOT - PLEASE STAY HYDRATED!!")
    
#### Problem 2 ####

print("=== Movie Theater Ticket System ===")

age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()
status = ""

ticket = 0

if age <= 12:
    ticket = 8.00
    status = "Junior "
elif age >= 65:
    ticket = 10.00
    status = "Senior "
else:
    ticket = 15.00

if day == "Tuesday" or day == "tuesday":
    ticket = 7.00
    print(f"Your ticket price: ${ticket} (Tuesday Special!)")
else:
    showtime = int(input("What time is the show? (0-23) "))
    if showtime < 17:
        ticket -= 3
        print(f"Your ticket price: ${ticket} ({status}Matinee)")
    else:
        print(f"Your ticket price: ${ticket}")

#### Problem 3 ####

print("=== Grade Calculator ===")

# Get three test scores
test1 = float(int(input("Enter Test 1 score (0-100): ")))
test2 = float(int(input("Enter Test 2 score (0-100): ")))
test3 = float(int(input("Enter Test 3 score (0-100): ")))

testSum = test1 + test2 + test3
average = testSum / 3

print("Average:", round(average))

if average >= 90:
    print("Letter Grade: A")
elif average >= 80:
    print("Letter Grade: B")
elif average >= 70:
    print("Letter Grade: C")
elif average >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")

if average >= 60:
    print("Status: PASSING")
else:
    print("Status: FAILING")
"""
#### Problem 4 ####

print("=== Password Strength Checker ===")

password = input("Enter a password to check: ")

# Initialize criteria counters
criteria_met = 0
feedback = []

if len(password) >= 8:
    criteria_met += 1

if password.lower() != password:
    criteria_met += 1
else:
    criteria_met -= 1

if password.upper() != password:
    criteria_met += 1
else:
    criteria_met -= 1

if any(char.isdigit() for char in password):
    criteria_met += 1
else:
    criteria_met -= 1

PasswordStrength = ""

if criteria_met <= 2:
    PasswordStrength = "Weak"
elif criteria_met == 3:
    PasswordStrength = "Fair"
elif criteria_met == 4:
    PasswordStrength = "Good"
elif criteria_met == 5:
    PasswordStrength = "Strong"

print("Password strength:", PasswordStrength)
print("Criteria met:", criteria_met, "out of 5")