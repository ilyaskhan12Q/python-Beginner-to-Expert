"""
=============================================================
  LESSON 04: Functions — Reusable Blocks of Code
=============================================================

REAL-WORLD ANALOGY:
  A function is like a recipe card.
  You write the steps ONCE on the card (define the function).
  Whenever you want to make the dish, you follow the card (call the function).

  You can also hand the recipe to someone else with different
  ingredients (arguments), and it still works!
=============================================================
"""

# ── 1. DEFINING AND CALLING A BASIC FUNCTION ──────────────────────────────
# Syntax:
#   def function_name(parameters):
#       """Optional description (docstring)."""
#       <code here>

def greet():
    """Print a simple greeting."""
    print("Hello! Welcome to Python.")

# Calling the function (running it):
greet()   # Output: Hello! Welcome to Python.
greet()   # You can call it as many times as you want


# ── 2. PARAMETERS AND ARGUMENTS ───────────────────────────────────────────
# Parameters = placeholders in the definition
# Arguments  = the actual values you pass when calling

def greet_person(name):         # 'name' is a parameter
    """Greet a specific person."""
    print(f"Hello, {name}! Great to meet you.")

greet_person("Alice")           # 'Alice' is the argument
greet_person("Bob")


# ── 3. MULTIPLE PARAMETERS ────────────────────────────────────────────────
def introduce(name, age, city):
    """Introduce a person with full details."""
    print(f"Hi! I'm {name}, {age} years old, from {city}.")

introduce("Alice", 30, "London")
introduce("Carlos", 25, "Madrid")


# ── 4. DEFAULT PARAMETER VALUES ───────────────────────────────────────────
# If a caller doesn't provide a value, the default is used.

def greet_with_title(name, title="Friend"):
    """Greet with an optional title."""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")                 # Uses default: Hello, Friend Smith!
greet_with_title("Smith", "Dr.")          # Overrides: Hello, Dr. Smith!
greet_with_title("Smith", title="Prof.")  # Keyword argument — very readable


# ── 5. RETURNING VALUES ───────────────────────────────────────────────────
# Use 'return' to send a result BACK to the caller.

def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(3, 7)
print(f"\n3 + 7 = {result}")   # 10

# Functions can return any type — including booleans
def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False


# ── 6. MULTIPLE RETURN VALUES ─────────────────────────────────────────────
# Python lets you return multiple values as a tuple.

def min_max(numbers):
    """Return the smallest and largest values in a list."""
    return min(numbers), max(numbers)

scores = [45, 98, 73, 12, 88]
lowest, highest = min_max(scores)   # "Unpacking" the returned tuple
print(f"\nLowest score:  {lowest}")
print(f"Highest score: {highest}")


# ── 7. SCOPE — Where Variables Live ───────────────────────────────────────
# Variables created INSIDE a function only exist inside that function.
# They disappear when the function finishes.

def make_sandwich():
    filling = "cheese"         # local variable — only exists here
    print(f"Making a {filling} sandwich.")

make_sandwich()
# print(filling)               # ← This would crash! 'filling' doesn't exist here

# Variables from OUTSIDE a function are accessible inside (but read carefully):
bread_type = "sourdough"       # global variable

def describe_sandwich():
    # We can READ global variables...
    print(f"Using {bread_type} bread.")

describe_sandwich()


# ── 8. DOCSTRINGS — Documenting Your Functions ────────────────────────────
# A docstring is a string right after the 'def' line.
# It explains what the function does. Always write one!

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m  (float): Height in metres.

    Returns:
        float: The BMI value, rounded to 1 decimal place.
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

bmi = calculate_bmi(70, 1.75)
print(f"\nBMI: {bmi}")


# ── 9. REAL-WORLD MINI PROJECT: Simple Calculator ─────────────────────────

def add(a, b):         return a + b
def subtract(a, b):    return a - b
def multiply(a, b):    return a * b
def divide(a, b):
    """Divide a by b. Returns None if b is zero."""
    if b == 0:
        print("⚠️  Cannot divide by zero!")
        return None
    return a / b

def run_calculator():
    """Interactive calculator using the functions above."""
    print("\n--- Simple Calculator ---")
    a = float(input("Enter first number:  "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ").strip()

    # Dictionary mapping operator symbols to functions — clean pattern!
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if op in operations:
        result = operations[op](a, b)
        if result is not None:
            print(f"Result: {a} {op} {b} = {result}")
    else:
        print("❌ Unknown operator.")

run_calculator()

print("\n✅ Lesson 04 complete! Move on to exercises/ex_04_functions.py")
