import itertools
import math
def validate_input(input_string):
    has_digit = any(char.isdigit() for char in input_string)
    has_special = any(not char.isalnum() for char in input_string)
    valid_length = len(input_string) >= 4
    return has_digit and has_special and valid_length
def calculate_password_strength(input_string):
    length = len(input_string)
    has_upper = any(char.isupper() for char in input_string)
    has_lower = any(char.islower() for char in input_string)
    has_digit = any(char.isdigit() for char in input_string)
    has_special = any(not char.isalnum() for char in input_string)
    length_score = min(40, (length - 4) * 5 + 20)  # Max length score = 40%
    variety_score = 0
    if has_upper: variety_score += 15
    if has_lower: variety_score += 15
    if has_digit: variety_score += 15
    if has_special: variety_score += 15
    total_strength = length_score + variety_score
    total_strength = min(100, total_strength)  # Cap at 100%

    return total_strength
def generate_password_combinations(input_string):
    password_combinations = []
    for r in range(4, len(input_string) + 1):
        combinations = [''.join(p) for p in itertools.permutations(input_string, r)]
        password_combinations.extend(combinations)
    return password_combinations
def calculate_total_combinations(input_string):
    n = len(input_string)
    # Calculate the sum of permutations for lengths >= 4
    total_combinations = sum(math.perm(n, r) for r in range(4, n + 1))
    return total_combinations
input_string = input("Enter your password: ")
if validate_input(input_string):
    password_combinations = generate_password_combinations(input_string)
    total_combinations = calculate_total_combinations(input_string)

    strength_percentage = calculate_password_strength(input_string)
    print(f"Total possible password combinations: {total_combinations}")
    print(f"Password strength: {strength_percentage:.2f}%")
else:
    print("Input must be at least 4 characters long and contain at least one number and one special character.")
