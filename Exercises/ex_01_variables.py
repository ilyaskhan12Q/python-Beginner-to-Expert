"""
=============================================================
  EXERCISE 01: Variables
  Based on: lessons/01_variables.py
=============================================================

Instructions:
  - Read each task carefully.
  - Write your code in the space provided (below each task).
  - Run the file to check your work:  python exercises/ex_01_variables.py
  - Solutions are in: solutions/sol_01_variables.py

TIP: Try to solve each exercise before looking at the solution!
=============================================================
"""

print("=" * 50)
print("  EXERCISE 01: Variables")
print("=" * 50)

# ─────────────────────────────────────────────────────────
# TASK 1 (Beginner)
# Create 4 variables to describe yourself:
#   - your_name    → a string with your first name
#   - your_age     → an integer with your age
#   - your_height  → a float with your height in metres
#   - is_student   → a boolean (True if you're a student)
#
# Then print a sentence using all 4 variables with an f-string.
# Expected output (example):
#   My name is Alex. I am 22 years old, 1.75m tall.
#   Am I a student? True
# ─────────────────────────────────────────────────────────

print("\n--- Task 1: Describing Yourself ---")
# ↓ Write your code below this line


# ─────────────────────────────────────────────────────────
# TASK 2 (Beginner)
# A shop has 50 apples. 15 are sold. 30 new ones arrive.
# Using ONLY the variable apple_count and arithmetic operators
# (+, -, +=, -=), track the changing stock.
#
# Expected output:
#   Start: 50 apples
#   After sale: 35 apples
#   After restock: 65 apples
# ─────────────────────────────────────────────────────────

print("\n--- Task 2: Apple Stock Tracker ---")
apple_count = 50
# ↓ Write your code below this line


# ─────────────────────────────────────────────────────────
# TASK 3 (Intermediate)
# Ask the user for:
#   - Their name
#   - Their birth year (as an integer — remember to convert!)
# Calculate their age (assume current year is 2025).
# Print a greeting with their name and calculated age.
#
# Example:
#   Enter your name: Jordan
#   Enter your birth year: 2000
#   Hello, Jordan! You are approximately 25 years old.
# ─────────────────────────────────────────────────────────

print("\n--- Task 3: Age Calculator ---")
CURRENT_YEAR = 2025
# ↓ Write your code below this line


# ─────────────────────────────────────────────────────────
# TASK 4 (Challenge)
# SWAP two variables WITHOUT using a third temporary variable.
# Python has an elegant way to do this in one line!
#
# Start with:
#   a = "hello"
#   b = "world"
# After swapping:
#   a should be "world"
#   b should be "hello"
#
# Print before and after to prove it worked.
# ─────────────────────────────────────────────────────────

print("\n--- Task 4: Variable Swap ---")
a = "hello"
b = "world"
print(f"Before: a={a}, b={b}")
# ↓ Swap them in ONE line below


print(f"After:  a={a}, b={b}")   # Should show: a=world, b=hello

print("\n✅ All tasks done? Check solutions/sol_01_variables.py")
