import random

temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]

total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)

highest = temperatures[0]
for temp in temperatures:
    if temp > highest:
        highest = temp

lowest = temperatures[0]
for temp in temperatures:
    if temp < lowest:
        lowest = temp

above_72 = 0
for temp in temperatures:
    if temp > 72:
        above_72 += 1

print("average:", average)
print("highest:", highest)
print("lowest:", lowest)
print("days above 72°F:", above_72)

print("\nFahrenheit to Celsius:")
for temp in temperatures:
    celsius = (temp - 32) * (5 / 9)
    print(f"{temp}°F  -->  {celsius:.2f}°C")


secret = random.randint(1, 20)

print("Guess a number from 1 to 20, you have 5 guesses.")
guesses = 5
print(secret)
numbers_guessed = []
while guesses != 0:
    guess = int(input("Please enter in a number: "))
    if guess > secret:
        guesses -= 1
        print("Too high! Try lower")
        print(f"you have {guesses} guesses left.")
        numbers_guessed.append(guess)
    elif guess < secret:
        guesses -= 1
        print("Too low! Try higher")
        print(f"you have {guesses} guesses left.")
        numbers_guessed.append(guess)
    elif guess == secret:
        guesses -= 1
        print(f"You guessed the number! You got it in {guesses + 1} guesse(s)!")
        if guesses == 4:
            print("Amazing! You're a mind reader!")
        elif guesses == 3 or guesses == 2:
            print("Great job!")
        elif guesses == 1 or guesses == 0:
            print("Great work!")
        print("Your guesses were:", numbers_guessed)
        break
    if guesses == 0:
        print("You have ran out of guesses!")
        print("Your guesses were:", numbers_guessed)
        print("Better luck next time!")
        break


grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]

total = 0
count = 0

letters = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

for g in grades:
    # Skip invalid grades (valid range: 0–100)
    if g < 0 or g > 100:
        print(f"Skipping invalid grade: {g}")
        continue

    # Update total and count
    total += g
    count += 1

    # Update highest and lowest
    if 90 <= g <= 100:
        letters["A"] += 1
    elif 80 <= g <= 89:
        letters["B"] += 1
    elif 70 <= g <= 79:
        letters["C"] += 1
    elif 60 <= g <= 69:
        letters["D"] += 1
    else:
        letters["F"] += 1

if count > 0:
    avg = total / count
    print("\n--- Valid Grade Statistics ---")
    print(f"Number of valid grades: {count}")
    print(f"Average grade: {avg:.2f}")

    print("\nLetter Grade Distribution:")
    for letter, num in letters.items():
        print(f"{letter}: {num}")