
# CS1300 - Homework #5: Advanced Control Structures
# Name: [Avery Layos]
# Date: [Submission Date]
# Description: Advanced conditional logic and validation


#### Problem 1 ####

print("=== SMART THERMOSTAT SYSTEM ===")

# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()

print("\n" + "Current Status:")
if current_temp <= 20:
    print(f"- Current temp: {current_temp}°F (TOO cold)")
elif current_temp <= 40:
    print(f"- Current temp: {current_temp}°F (cold)")
elif current_temp <= 50:
    print(f"- Current temp: {current_temp}°F (cool)")
elif current_temp <= 65:
    print(f"- Current temp: {current_temp}°F (warm)")
elif current_temp <= 80:
    print(f"- Current temp: {current_temp}°F (hot)")
elif current_temp > 80:
    print(f"- Current temp: {current_temp}°F (TOO hot)")

if 68 <= current_temp <= 76:
    print("- Current temp range: comfortable")
else:
    print("- Current temp range: uncomfortable")

if hour >= 22 or hour <= 6:
    nightMode = True
    print("- Night mode: ACTIVE (reducing target by 3°F)")
else:
    nightMode = False
    print("- Night mode: INACTIVE")

season_caps = {
        "summer": 75,
        "winter": 70,
        "spring": 72,
        "fall": 72
    }

season_cap = season_caps.get(season.lower(), desired_temp)

print(f"- Season: {season} (max {season_cap}°F allowed)")

print("\n" + "Adjustments:")
print(f"- Desired: {desired_temp}°F")

night_adjust = desired_temp - 3

if nightMode == True:
    print(f"- Night adjustment: {night_adjust = desired_temp - 3}°F")

print("- Seasonal limit applied:", desired_temp)

target_Temp = min(desired_temp, season_cap)


print("- Final target:", target_Temp)

difference = target_Temp - current_temp

if difference < 1:
    efficiency = "EXCELLENT"
elif difference < 3:
    efficiency = "GOOD"
elif difference < 5:
    efficiency = "FAIR"
else:
    efficiency = "POOR"

print("Heating required:", )

#### Problem 2 ####

from ast import pattern


print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")

# Initialize score
score = 0

# YOUR CODE HERE
# Use conditional expressions for each check
length_points = 0
# Check length (use conditional expression)

if len(password) >= 16:
    print("✓ Length:", len(password), "characters (30/30 points)")
    length_points = 30
elif len(password) >= 12:
    print("✓ Length:",len(password), "characters (20/30 points)")
    length_points = 20
elif len(password) >= 8:
    print("✓ Length:", len(password), "characters (10/30 points)")
    length_points = 10


upper_points = 0
# Check for uppercase (use conditional expression)
if password != password.lower():
    print("✓ Uppercase letters: Yes (15/15 points)")
    upper_points = 15
#has_upper

lower_points = 0
# Check for lowercase
if password != password.upper():
    print("✓ Lowercase letters: Yes (15/15 points)")
    lower_points = 15

# Check for numbers
digit_points = 0
if any(c.isdigit() for c in password):
    print("✓ Numbers: Yes (15/15 points)")
    digit_points = 15

# Check for special characters
special_points = 0
if not password.isalnum():
    print("✓ Special characters: Yes (15/15 points)")
    special_points = 15

# Check for common patterns
pattern_points = 0
common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
if has_pattern:
    print(f"✗ Common patterns detected: {has_pattern} (-10 points)")
    pattern_points = -10

total = score + length_points + upper_points + lower_points + digit_points + special_points + pattern_points

if total >= 90:
    strength = "AMAZING"
elif total >= 70:
    strength = "GOOD"
elif total >= 50:
    strength = "OK"
elif total >= 30:
    strength = "BAD"
else:
    strength = "TERRIBLE"

# Calculate total score and determine strength level
print("Total score:", score + length_points + upper_points + lower_points + digit_points + special_points + pattern_points)
print("Strength level:", strength)
# Display detailed analysis


#### Problem 3 ####

print("=== GRADE VALIDATION SYSTEM ===")

# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))

scores = [test1, test2, test3, test4]

avg = (test1 + test2 + test3 + test4) / 4
highest_grade = max(test1, test2, test3, test4)
lowest_grade = min(test1, test2, test3, test4)

# check for suspicious patterns

if (test1 == test2 == test3 == test4):
    score_identical = True
else:
    score_identical = False

huge_jump = any(abs(scores[i] - scores[i + 1]) > 40 for i in range(3))

if scores == 100:
    all_perfect = True
else:
    all_perfect = False

print("\n" + "Validation Results:")

if (0 <= test1 <= 100 and
    0 <= test2 <= 100 and
    0 <= test3 <= 100 and
    0 <= test4 <= 100):
    valid = True
else:
    valid = False

if valid == False:
    print("X All scores are not valid (0-100)")
elif score_identical == True:
    print("All scores are identical - possible cheating")
elif huge_jump:
    print("Huge jump detected between tests (>40 points)")
elif all_perfect == True:
    print("All scores are perfect 100s - unusual scores")
else:
    print("✓ All scores in valid range (0-100)")

    if scores[-1] - scores[0] >= 15:
        trend = "IMPROVING"
    elif scores[0] - scores[-1] >= 15:
        trend = "DECLINING"
    else:
        trend = "STABLE"

    if avg >= 90:
        letter_grade = "A"
        status = "PASSING"
    elif avg >= 80:
        letter_grade = "B"
        status = "PASSING"
    elif avg >= 70:
        letter_grade = "C"
        status = "PASSING"
    elif avg >= 60:
        letter_grade = "D"
        status = "PASSING"
    else:
        letter_grade = "F"
        status = "FAILING"

    if trend == "IMPROVING" and status == "PASSING":
        print("✓ Steady improvement detected (+{} points overall)".format(scores[-1] - scores[0]))
        message = "Consistent improvement shown!"
    elif trend == "IMPROVING" and status == "FAILING":
        print("- Sight improvement detected (+{} points overall)".format(scores[-1] - scores[0]))
        message = "A little improvement but still failing."
    elif trend == "DECLINING" and status == "FAILING":
        print("X Decline detected ({} points drop)".format(scores[0] - scores[-1]))
        message = "Consistent decline shown needs to really improve."
    elif trend == "DECLINING" and status == "PASSING":
        print("X Decline detected ({} points drop)".format(scores[0] - scores[-1]))
        message = "Still passing but really needs to pick up."
    else:
        print("✓ Performance stable")
        message = "Just need a little more improvement."

    print("\n" + "Statistics:")
    print("- Average:", avg)
    print("- Highest:", highest_grade)
    print("- Lowest:", lowest_grade)
    print("- Trend:", trend)

    print("\n" + "Grade:", letter_grade)
    print("Status:", status)
    print("Performance:", message)


#### Problem 4 ####

print("=== EVENT SCHEDULING SYSTEM ===")

# Event 1
print("\nEVENT 1 DETAILS:")
event1_name = input("Event name: ")
event1_day = input("Day (Mon-Sun): ").lower()[:3] # First 3 letters
event1_start = float(input("Start time (0-24): "))
event1_end = float(input("End time (0-24): "))

# Event 2
print("\nEVENT 2 DETAILS:")
event2_name = input("Event name: ")
event2_day = input("Day (Mon-Sun): ").lower()[:3]
event2_start = float(input("Start time (0-24): "))
event2_end = float(input("End time (0-24): "))

# YOUR CODE HERE
# 1. Validate times are in range 0-24
if (0 <= event1_start <= 24 and 0 <= event1_end <= 24 and 0 <= event2_start <= 24 and 0 <= event2_start <= 24):
    times_valid = True
else:
    time_valid = False
    print("\nPlease put valid start and end times (0-24)")

    # Event 1
    print("\nEVENT 1 DETAILS:")
    event1_start = float(input("Start time (0-24): "))
    event1_end = float(input("End time (0-24): "))

    # Event 2
    print("\nEVENT 2 DETAILS:")
    event2_start = float(input("Start time (0-24): "))
    event2_end = float(input("End time (0-24): "))

# 2. Validate end time > start time for each event
if (event1_start < event1_end and event2_start < event2_end):
    endGreater_thanStart = True
else:
    endGreater_thanStart = False
    print("\nPlease put a start time that is smaller than the end time (0-24)")

    # Event 1
    print("\nEVENT 1 DETAILS:")
    event1_start = float(input("Start time (0-24): "))
    event1_end = float(input("End time (0-24): "))

    # Event 2
    print("\nEVENT 2 DETAILS:")
    event2_start = float(input("Start time (0-24): "))
    event2_end = float(input("End time (0-24): "))

# 3. Check for conflicts using complex conditions
# 4. Calculate gap between events if same day
# 5. Check for early/late scheduling issues

# Valid days
valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# Validation using chained comparisons
if event1_day in valid_days and event2_day in valid_days:
    eventDays_valid = True
else:
    eventDays_valid = False
    print("\nPlease put valid days (Mon-Sun)")

    # Event 1
    print("\nEVENT 1 DETAILS:")
    event1_day = input("Day (Mon-Sun): ").lower()[:3] # First 3 letters

    # Event 2
    print("\nEVENT 2 DETAILS:")
    event2_day = input("Day (Mon-Sun): ").lower()[:3]


# Check for conflicts
if (event1_day == event2_day):
    same_day = True
    if ((event1_start == event2_end and event2_start == event1_end) or (event2_start < event1_end)):
        print("\nEvent 1 and 2 start times and end times overlap!")
        print("Please put times that do not overlap")

        # Event 1
        print("\nEVENT 1 DETAILS:")
        event1_start = float(input("Start time (0-24): "))
        event1_end = float(input("End time (0-24): "))

        # Event 2
        print("\nEVENT 2 DETAILS:")
        event2_start = float(input("Start time (0-24): "))
        event2_end = float(input("End time (0-24): "))


print("\nSchedule Analysis:")

if eventDays_valid == True:
    print("✓ Both events have valid times")

if (event1_end == event2_start and same_day == True):
    backtoback = True
    print("⚠ Events are back-to-back (0 minutes between)")

if (event1_start and event1_end != event2_start and event2_end):
    print("✓ no direct time conflict")

event1_Time = event1_end - event1_start
event2_Time = event2_end - event2_start

print(f"\nEvent 1: {event1_name}")
if (event1_Time >= 1):
    print(f"- {event1_day} {event1_start} - {event1_end} ({event1_Time} hour(s))")
else:
    print(f"- {event1_day} {event1_start} - {event1_end} ({event1_Time} minute(s))")

print(f"\nEvent 2: {event2_name}")
if (event2_Time >= 1):
    print(f"- {event2_day} {event2_start} - {event2_end} ({event2_Time} hour(s))")
else:
    print(f"- {event2_day} {event2_start} - {event2_end} ({event2_Time} minute(s))")

if (event1_Time + event2_Time) >= 1:
    print(f"\nTotal time commitment: {event1_Time + event2_Time} hour(s)")
else:
    print(f"\nTotal time commitment: {event1_Time + event2_Time} minute(s)")

if backtoback == True:
    rec_msg = "Recommendation: consider adding buffer time between events"

    


