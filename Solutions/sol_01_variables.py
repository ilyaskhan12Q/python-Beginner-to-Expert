"""
=============================================================
  SOLUTION 01: Variables
=============================================================
  Only look at this after attempting the exercises yourself!
=============================================================
"""

print("=" * 50)
print("  SOLUTION 01: Variables")
print("=" * 50)

# ── TASK 1 ────────────────────────────────────────────────
print("\n--- Task 1: Describing Yourself ---")

your_name   = "Alex"
your_age    = 22
your_height = 1.75
is_student  = True

print(f"My name is {your_name}. I am {your_age} years old, {your_height}m tall.")
print(f"Am I a student? {is_student}")


# ── TASK 2 ────────────────────────────────────────────────
print("\n--- Task 2: Apple Stock Tracker ---")

apple_count = 50
print(f"Start: {apple_count} apples")

apple_count -= 15
print(f"After sale: {apple_count} apples")

apple_count += 30
print(f"After restock: {apple_count} apples")


# ── TASK 3 ────────────────────────────────────────────────
print("\n--- Task 3: Age Calculator ---")

CURRENT_YEAR = 2025
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = CURRENT_YEAR - birth_year

print(f"Hello, {name}! You are approximately {age} years old.")


# ── TASK 4 ────────────────────────────────────────────────
print("\n--- Task 4: Variable Swap ---")

a = "hello"
b = "world"
print(f"Before: a={a}, b={b}")

# Python's elegant tuple unpacking — swap in one line!
a, b = b, a

print(f"After:  a={a}, b={b}")
