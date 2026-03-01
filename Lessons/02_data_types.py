"""
=============================================================
  LESSON 02: Data Types — The Kinds of Values Python Knows
=============================================================

REAL-WORLD ANALOGY:
  Imagine different containers in a kitchen:
  - A jar for text (strings):      "Alice", "Hello, World!"
  - A measuring cup for integers:  42, -7, 0
  - A scale for decimals (floats): 3.14, 99.9, -0.5
  - A light switch for booleans:   True, False (on/off)

  Python needs to know WHAT KIND of value it's working with
  because you can't multiply a name by 3 (or can you...?)
=============================================================
"""

# ── 1. STRINGS (str) — Text ────────────────────────────────────────────────
# Any text surrounded by quotes (single ' or double ")

first_name = "Alice"
last_name = 'Wonderland'
empty_string = ""

# Combining strings with + is called "concatenation"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")                    # Alice Wonderland

# String methods — built-in tools for working with text
print(full_name.upper())                             # ALICE WONDERLAND
print(full_name.lower())                             # alice wonderland
print(full_name.replace("Alice", "Bob"))             # Bob Wonderland
print(len(full_name))                                # 16  (number of characters)

# Multiline strings use triple quotes
message = """
Hello!
This is a
multiline string.
"""
print(message)

# Repeating strings (yes, this works!)
separator = "-" * 30
print(separator)  # ------------------------------

# ── 2. INTEGERS (int) — Whole Numbers ─────────────────────────────────────
age = 25
temperature = -3
big_number = 1_000_000  # Underscores make large numbers readable

print(f"\nAge: {age}")
print(f"Temperature: {temperature}°C")
print(f"Big number: {big_number}")

# Integer math
print(10 + 3)   # 13  → addition
print(10 - 3)   # 7   → subtraction
print(10 * 3)   # 30  → multiplication
print(10 ** 3)  # 1000 → exponentiation (10 to the power of 3)
print(10 // 3)  # 3   → floor division (whole number result only)
print(10 % 3)   # 1   → modulo (the remainder after dividing)

# ── 3. FLOATS (float) — Decimal Numbers ───────────────────────────────────
price = 9.99
pi = 3.14159
negative_temp = -7.5

print(f"\nPrice: ${price}")
print(f"Pi: {pi}")
print(f"Temperature: {negative_temp}°C")

# Float and int math together → result is a float
result = 10 / 3         # Regular division ALWAYS gives a float
print(f"10 / 3 = {result}")           # 3.3333...
print(f"10 / 3 = {result:.2f}")       # 3.33  (rounded to 2 decimal places)

# ── 4. BOOLEANS (bool) — True or False ────────────────────────────────────
is_raining = True
has_umbrella = False
is_sunny = not is_raining  # "not" flips True → False, and False → True

print(f"\nIs it raining? {is_raining}")
print(f"Do I have an umbrella? {has_umbrella}")
print(f"Is it sunny? {is_sunny}")

# Comparisons produce booleans
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True  (== means "is equal to")
print(5 != 3)   # True  (!= means "is NOT equal to")

# ── 5. CHECKING THE TYPE OF A VALUE ───────────────────────────────────────
# Use type() to ask Python: "What kind of thing is this?"

print("\n--- Type Checking ---")
print(type("hello"))        # <class 'str'>
print(type(42))             # <class 'int'>
print(type(3.14))           # <class 'float'>
print(type(True))           # <class 'bool'>

# ── 6. CONVERTING BETWEEN TYPES ───────────────────────────────────────────
# Also called "type casting"

age_as_text = "25"              # This is a string "25", not the number 25
age_as_number = int(age_as_text)  # Convert to integer

print(f"\nString '25' + 1 = ERROR (can't add text and number)")
print(f"Integer 25 + 1  = {age_as_number + 1}")   # 26

# input() always returns a string — you must convert if you want math!
print("\n--- User Input with Type Conversion ---")
raw = input("Enter your age: ")           # Always returns a string
age = int(raw)                            # Convert to int for math
print(f"In 10 years you'll be {age + 10}")

print("\n✅ Lesson 02 complete! Move on to exercises/ex_02_data_types.py")
