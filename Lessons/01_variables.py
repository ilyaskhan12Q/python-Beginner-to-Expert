"""
=============================================================
  LESSON 01: Variables — Labeled Boxes for Your Data
=============================================================

REAL-WORLD ANALOGY:
  Think of a variable like a sticky note on a box.
  The sticky note is the NAME, and what's inside the box is the VALUE.

  box labeled "player_score" → contains the number 0
  box labeled "player_name"  → contains the text "Alice"

You can look inside the box, change the contents,
or use the contents in calculations — anytime you want.
=============================================================
"""

# ── 1. CREATING VARIABLES ──────────────────────────────────────────────────
# Syntax:  variable_name = value
# The "=" sign means "assign this value to this name"

player_name = "Alice"       # A word/text variable (called a "string")
player_score = 0            # A whole number (called an "integer")
player_health = 100.0       # A decimal number (called a "float")
is_game_over = False        # True or False only (called a "boolean")

# ── 2. PRINTING VARIABLES ─────────────────────────────────────────────────
# Use print() to display a value in the terminal

print(player_name)     # Output: Alice
print(player_score)    # Output: 0
print(player_health)   # Output: 100.0
print(is_game_over)    # Output: False

# ── 3. BUILDING MESSAGES WITH VARIABLES ───────────────────────────────────
# f-strings (formatted strings) let you embed variables inside text.
# Put an f before the quote, and wrap variable names in { }

print(f"Player: {player_name}")
print(f"Score:  {player_score}")
print(f"Health: {player_health}")

# ── 4. CHANGING VARIABLE VALUES ───────────────────────────────────────────
# You can overwrite a variable at any time — just assign again.

player_score = 50           # Score has changed
player_health = 75.5        # Health has changed

print(f"\nUpdated Score:  {player_score}")
print(f"Updated Health: {player_health}")

# ── 5. MATH WITH VARIABLES ────────────────────────────────────────────────
bonus_points = 20
player_score = player_score + bonus_points  # Add bonus to score
print(f"\nScore after bonus: {player_score}")   # Output: 70

# Shorthand (does the same thing):
player_score += 10  # Same as: player_score = player_score + 10
print(f"Score after shorthand: {player_score}")  # Output: 80

# ── 6. GETTING INPUT FROM THE USER ────────────────────────────────────────
# input() pauses the program and waits for the user to type something.
# Whatever they type comes back as a string (text).

print("\n--- Interactive Section ---")
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python.")

# ── 7. NAMING RULES ───────────────────────────────────────────────────────
# Good variable names:
#   player_name    ✅  (snake_case — the Python standard)
#   total_score    ✅
#   isGameOver     ✅  (camelCase — works but less Pythonic)
#
# Bad variable names:
#   2fast          ❌  (can't START with a number)
#   my-var         ❌  (hyphens not allowed, use underscores)
#   class          ❌  (reserved Python keyword)

# TIP: Use descriptive names. "score" is better than "s".
# Your future self will thank you.

print("\n✅ Lesson 01 complete! Move on to exercises/ex_01_variables.py")
