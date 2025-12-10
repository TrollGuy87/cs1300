def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count
        
print(count_positive([5, -2, 0, 3, -1, 8]))
print(count_positive([-1,-2,-3]))
print(count_positive([10, 20, 30]))
print(count_positive([]))

def get_age_group(age):
    if age > 59:
        return "Senior"
    elif age >= 20:
        return "Adult"
    elif age >= 13:
        return "Teen"
    else:
        return "Child"
    
def count_age_groups(ages):
    groups = {"Child": 0, "Teen": 0, "Adult": 0, "Senior": 0}

    for age in ages:
        category = get_age_group(age)
        groups[category] += 1
    
    return groups

print(get_age_group(5))
print(get_age_group(15))
print(get_age_group(30))
print(get_age_group(65))

ages_list = [5, 15, 25, 35, 65, 8, 18, 70]
print(count_age_groups(ages_list))

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("Mom"))
print(is_palindrome("noon"))
print(is_palindrome("python"))

def create_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        line = ""
        for x in range(1, i + 1):
            line += str(x) + " "
        pattern.append(line.strip())
    return pattern

def print_pattern(n):
    rows = create_pattern(n)
    for row in rows:
        print(row)

print_pattern(3)

def reverse_list(items):
    reverse = items[::-1]
    return reverse

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["a", "b", "c"]))
print(reverse_list([10]))
print(reverse_list([]))

