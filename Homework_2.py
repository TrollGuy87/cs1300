#python
import random


print("\n" + "=" * 50)
print("      Problem 1: Personal Finance Calculator")
print("=" * 50)

monthlyIncome = float(input("\n" +"Enter your monthly income: "))
Rent = float(input("Enter rent cost: "))
foodExpenses = float(input("Enter food expenses: "))
transportCost = float(input("Enter your transport cost: "))
otherExpenses = float(input("Enter any other expenses: "))

print("\n" + "=" * 50)
print("Monthly Budget Report")
print("=" * 50)

print("Income:            $", monthlyIncome)
print("-" * 40)
print("Expenses:")
print(" Housing:          $", Rent)
print(" Food:             $", foodExpenses)
print(" Transportation:   $", transportCost)
print(" Other:            $", otherExpenses)
print("-" * 40)
totalExpense = Rent + foodExpenses + transportCost + otherExpenses
print("Total Expenses:    $", totalExpense)
Remaining = monthlyIncome - totalExpense
print("Remaining Balance: $", Remaining)
print("Saving rate: ", Remaining / monthlyIncome,"%")

print("\n" + "=" * 50)
print("      Problem 2: Grading Criteria")
print("=" * 50)


testScore = []
for i in range(5):
    testScore.append(random.randint(1, 100))

print("\n" + "The test score of the five students are:", testScore)

scoreSum = sum(testScore)
print("\n" + "The total sum of these scores are:", scoreSum)

overallAverage = scoreSum / len(testScore)
print("\n" + "The overall average of these scores is:", overallAverage)

maxScore = max(testScore)
print("\n" + "The highest score is:", maxScore)


testScores = []
for i in range(5):
    grades = float(input("\n" + f"Enter score {i + 1} (0-100): "))
    while grades < 0 or grades > 100:
        print("Invalid score plese enter number between 1 and 100.")
        grades = float(input("\n" + f"Enter score {i + 1} (0-100): "))
    testScores.append(grades)

print("\n" + "=" * 50)
print("Grade report:")
print("=" * 50)
print("Test Scores Entered:")
for i in range(5):
    print(f"Test {i + 1}:      {testScores[i]}/100")
print("\n" + "=" * 50)

scoreSum = sum(testScores)
print("\n" + f"Total points:          {scoreSum}/500")

Average = scoreSum / len(testScores)
print("Average score:        ", Average)

Overall = (scoreSum / 500) * 100
print(f"Overall grade:         {Overall}%")

pointsNeeded = (0.9 * 500) - scoreSum

print("Points needed for 90%:", pointsNeeded)

print("\n" + "=" * 50)
print("Problem 3: Time Zone Converter")
print("=" * 50)


for i in range(1):
    hour = int(input("What is the current hour? (0-23): "))
    while hour < 0 or hour > 23:
        print("Invalid score plese enter the hour in 24-hour format.")
        hour = int(input("What is the current hour? (0-23): "))
        
for i in range(1):
    minute = int(input("What is the current minute? (0-59): "))
    while minute < 0 or minute > 59:
        print("Invalid score plese enter a minute between 0-59.")
        minute = int(input("What is the current minute? (0-59): "))

def format_time(hour, minute):
    return f"{hour:02d}:{minute:02d}"

def to_12_hour_format(hour, minute):
    time = "AM" if hour < 12 else "PM"
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12
    return f"{hour_12:02d}:{minute:02d} {time}"

est_hour = hour % 24
cst_hour = (hour - 1) % 24
mst_hour = (hour - 2) % 24
pst_hour = (hour - 3) % 24

print(f"EST: {format_time(est_hour, minute)} | {to_12_hour_format(est_hour, minute)} |")
print(f"CST: {format_time(cst_hour, minute)} | {to_12_hour_format(cst_hour, minute)} |")
print(f"MST: {format_time(mst_hour, minute)} | {to_12_hour_format(mst_hour, minute)} |")
print(f"PST: {format_time(pst_hour, minute)} | {to_12_hour_format(pst_hour, minute)} |")


print("\n" + "=" * 50)
print("Problem 4: Recipe Scaler")
print("=" * 50)

def get_recipe_input():
    original_servings = int(input("Enter original serving size: "))
    desired_servings = int(input("Enter desired serving size: "))
    
    ingredients = []
    print("\nEnter 5 ingredients:")
    for i in range(5):
        name = input(f"Ingredient {i+1} name: ")
        amount = float(input(f"Amount of {name}: "))
        unit = input(f"Unit for {name} (e.g., cups, tbsp): ")
        ingredients.append({'name': name, 'amount': amount, 'unit': unit})
    
    return original_servings, desired_servings, ingredients

def scale_ingredients(original_servings, desired_servings, ingredients):
    scale_factor = desired_servings / original_servings
    scaled_ingredients = []
    for item in ingredients:
        scaled_amount = item['amount'] * scale_factor
        scaled_ingredients.append({
            'name': item['name'],
            'original_amount': item['amount'],
            'scaled_amount': scaled_amount,
            'unit': item['unit']
        })
    return scaled_ingredients

def display_recipes(scaled_ingredients):
    print("\n--- Recipe Comparison ---")
    print(f"{'Ingredient':<15} | {'Original':<15} | {'Scaled':<15}")
    print("-" * 50)
    for item in scaled_ingredients:
        original = f"{item['original_amount']} {item['unit']}"
        scaled = f"{item['scaled_amount']:.2f} {item['unit']}"
        print(f"{item['name']:<15} | {original:<15} | {scaled:<15}")

original_servings, desired_servings, ingredients = get_recipe_input()
scaled_ingredients = scale_ingredients(original_servings, desired_servings, ingredients)
display_recipes(scaled_ingredients)