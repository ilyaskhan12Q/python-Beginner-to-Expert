"""
=============================================================
  LESSON 03: Control Flow — Making Decisions & Repeating
=============================================================

REAL-WORLD ANALOGY:
  IF/ELSE is like a crossroads sign:
    "If you have a ticket → go to the show
     Otherwise           → go back home"

  LOOPS are like a playlist:
    "Play every song in the playlist"        ← for loop
    "Keep playing until the battery dies"    ← while loop
=============================================================
"""

# ── 1. IF / ELIF / ELSE ────────────────────────────────────────────────────
# Syntax:
#   if <condition>:       ← runs if condition is True
#       ...
#   elif <condition>:     ← checked only if the 'if' was False
#       ...
#   else:                 ← runs if ALL conditions above were False
#       ...

temperature = 22  # degrees Celsius

if temperature > 30:
    print("It's hot! Wear shorts.")
elif temperature > 20:
    print("Nice weather! A t-shirt will do.")
elif temperature > 10:
    print("A bit cool. Bring a jacket.")
else:
    print("It's cold! Bundle up.")

# ── 2. COMPARISON OPERATORS ───────────────────────────────────────────────
# Used inside conditions to compare values

#  ==   equal to              5 == 5  → True
#  !=   not equal to          5 != 3  → True
#  >    greater than          5 > 3   → True
#  <    less than             5 < 3   → False
#  >=   greater or equal to   5 >= 5  → True
#  <=   less or equal to      5 <= 4  → False

# ── 3. LOGICAL OPERATORS ──────────────────────────────────────────────────
# Combine multiple conditions with: and, or, not

has_ticket = True
is_vip = False

if has_ticket and is_vip:
    print("Welcome to the VIP area!")
elif has_ticket and not is_vip:
    print("Welcome! Please find a regular seat.")
else:
    print("Sorry, you need a ticket to enter.")

# ── 4. FOR LOOP — Repeat over a sequence ──────────────────────────────────
# "For each item in this collection, do something."

fruits = ["apple", "banana", "cherry"]

print("\n--- Fruit List ---")
for fruit in fruits:
    print(f"  I like {fruit}")

# range() generates a sequence of numbers
print("\n--- Counting with range() ---")
for i in range(5):         # 0, 1, 2, 3, 4  (starts at 0 by default)
    print(f"  Count: {i}")

print("\n--- range(start, stop, step) ---")
for i in range(1, 10, 2):  # start=1, stop=10, step=2
    print(f"  Odd number: {i}")   # 1, 3, 5, 7, 9

# enumerate() gives you both the index AND the value
print("\n--- enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# ── 5. WHILE LOOP — Repeat while a condition is True ──────────────────────
# "Keep going as long as this condition holds."

print("\n--- Countdown ---")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1   # Same as: count = count - 1
print("  🚀 Blastoff!")

# ── 6. LOOP CONTROLS: break and continue ──────────────────────────────────
# break    → immediately exit the loop
# continue → skip the rest of THIS iteration, jump to the next

print("\n--- break example: find first even number ---")
numbers = [1, 3, 5, 4, 7, 9]
for num in numbers:
    if num % 2 == 0:        # If the number is even...
        print(f"  Found it: {num}")
        break               # ...stop looking

print("\n--- continue example: skip odd numbers ---")
for num in range(1, 8):
    if num % 2 != 0:        # If the number is odd...
        continue            # ...skip it and go to the next one
    print(f"  Even: {num}")

# ── 7. PUTTING IT TOGETHER — Simple Number Guessing Game ──────────────────
import random

print("\n--- Number Guessing Game ---")
secret = random.randint(1, 10)   # Pick a random number between 1 and 10
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input(f"Guess a number (1–10), {max_attempts - attempts} tries left: "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Correct! You got it in {attempts} attempt(s)!")
        break
    elif guess < secret:
        print("  Too low!")
    else:
        print("  Too high!")
else:
    # This else belongs to the while loop — runs only if the loop
    # completed WITHOUT hitting a break
    print(f"❌ Out of attempts! The number was {secret}.")

print("\n✅ Lesson 03 complete! Move on to exercises/ex_03_control_flow.py")
