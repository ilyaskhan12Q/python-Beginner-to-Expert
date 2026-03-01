"""
=============================================================
  EXERCISE 05: Lists & Dictionaries
  Based on: lessons/05_lists_and_dicts.py
=============================================================
"""

print("=" * 50)
print("  EXERCISE 05: Lists & Dictionaries")
print("=" * 50)

# ─────────────────────────────────────────────────────────
# TASK 1 (Beginner)
# Start with: numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Using list methods (not sorting by hand!):
#   a) Print the number of times 5 appears
#   b) Print the list sorted in ascending order
#   c) Print the list reversed
#   d) Print the sum, min, and max
# ─────────────────────────────────────────────────────────
print("\n--- Task 1: List Operations ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# ↓ Your code here


# ─────────────────────────────────────────────────────────
# TASK 2 (Intermediate)
# Use a LIST COMPREHENSION to:
#   a) Create a list of squares from 1 to 10
#   b) Filter only the even squares from that list
#   c) Create a list of the WORDS (not chars) in a sentence
#      that have more than 4 letters
#
# sentence = "The quick brown fox jumps over the lazy dog"
# ─────────────────────────────────────────────────────────
print("\n--- Task 2: List Comprehensions ---")
sentence = "The quick brown fox jumps over the lazy dog"
# ↓ Your code here


# ─────────────────────────────────────────────────────────
# TASK 3 (Intermediate)
# Build a word frequency counter.
# Given a sentence, create a dictionary where:
#   key = word (lowercased)
#   value = how many times it appears
# Then print the TOP 3 most common words.
#
# text = "to be or not to be that is the question to be"
# ─────────────────────────────────────────────────────────
print("\n--- Task 3: Word Frequency ---")
text = "to be or not to be that is the question to be"
# ↓ Your code here


# ─────────────────────────────────────────────────────────
# TASK 4 (Challenge)
# Build a simple phonebook using a dictionary of dictionaries.
# Contacts: Alice (555-1234, alice@mail.com),
#           Bob (555-5678, bob@mail.com),
#           Carlos (555-9999, carlos@mail.com)
#
# Write functions to:
#   a) lookup(name) → print contact details or "Not found"
#   b) add_contact(name, phone, email) → add to phonebook
#   c) delete_contact(name) → remove if exists
#
# Then write a simple interactive loop that lets the user
# choose: lookup / add / delete / quit
# ─────────────────────────────────────────────────────────
print("\n--- Task 4: Phonebook ---")
phonebook = {
    "Alice":  {"phone": "555-1234", "email": "alice@mail.com"},
    "Bob":    {"phone": "555-5678", "email": "bob@mail.com"},
    "Carlos": {"phone": "555-9999", "email": "carlos@mail.com"},
}
# ↓ Your code here


print("\n✅ All tasks done? Check solutions/sol_05_lists_and_dicts.py")
