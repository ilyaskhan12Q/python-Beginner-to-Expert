"""
=============================================================
  EXERCISE 04: Functions
  Based on: lessons/04_functions.py
=============================================================
"""

print("=" * 50)
print("  EXERCISE 04: Functions")
print("=" * 50)

# ─────────────────────────────────────────────────────────
# TASK 1 (Beginner)
# Write a function is_palindrome(word) that returns True if
# the word reads the same forwards and backwards.
# (Hint: "racecar"[::-1] reverses a string)
#
# Test cases:
#   is_palindrome("racecar") → True
#   is_palindrome("python")  → False
#   is_palindrome("madam")   → True
# ─────────────────────────────────────────────────────────
print("\n--- Task 1: Palindrome Checker ---")
# ↓ Your code here


# ─────────────────────────────────────────────────────────
# TASK 2 (Intermediate)
# Write a function celsius_to_all(celsius) that returns a
# dictionary with celsius, fahrenheit, and kelvin values.
#
# Test:
#   result = celsius_to_all(100)
#   → {'celsius': 100, 'fahrenheit': 212.0, 'kelvin': 373.15}
# ─────────────────────────────────────────────────────────
print("\n--- Task 2: Multi-Unit Converter ---")
# ↓ Your code here


# ─────────────────────────────────────────────────────────
# TASK 3 (Intermediate)
# Write a function grade_summary(scores) that:
#   - Takes a list of scores (0–100)
#   - Returns a dict: {"average": ..., "highest": ...,
#                      "lowest": ..., "grade": ...}
#   - Grade: A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
#
# scores = [78, 92, 65, 88, 55]
# Expected: {'average': 75.6, 'highest': 92, 'lowest': 55, 'grade': 'C'}
# ─────────────────────────────────────────────────────────
print("\n--- Task 3: Grade Summary ---")
# ↓ Your code here


# ─────────────────────────────────────────────────────────
# TASK 4 (Challenge)
# Write a recursive function factorial(n) that calculates n!
# (Without using math.factorial)
#
# Recursive means: the function calls ITSELF with a smaller value.
# Base case: factorial(0) = 1
# Recursive case: factorial(n) = n * factorial(n - 1)
#
# factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
# ─────────────────────────────────────────────────────────
print("\n--- Task 4: Recursive Factorial ---")
# ↓ Your code here


print("\n✅ All tasks done? Check solutions/sol_04_functions.py")
