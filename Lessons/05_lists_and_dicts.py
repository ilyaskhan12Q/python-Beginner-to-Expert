"""
=============================================================
  LESSON 05: Lists & Dictionaries — Storing Collections
=============================================================

REAL-WORLD ANALOGY:
  LIST       = a numbered shopping list
               Index 0: eggs | Index 1: milk | Index 2: bread
               Order matters. You access items by position.

  DICTIONARY = a contact book
               "Alice" → 555-1234
               "Bob"   → 555-5678
               Each entry has a KEY (name) and a VALUE (number).
=============================================================
"""

# ══════════════════════════════════════════════════════════════════════════
#  PART 1: LISTS
# ══════════════════════════════════════════════════════════════════════════

# ── 1. CREATING LISTS ─────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [42, "hello", True, 3.14]   # Lists can hold different types
empty = []

print("Fruits:", fruits)
print("Numbers:", numbers)

# ── 2. ACCESSING ITEMS — Indexing ─────────────────────────────────────────
# Indexes START at 0, not 1.

print("\n--- Indexing ---")
print(fruits[0])    # apple  (first item)
print(fruits[1])    # banana (second item)
print(fruits[-1])   # cherry (LAST item — negative indexing counts from end)
print(fruits[-2])   # banana (second to last)

# ── 3. SLICING — Getting a Sub-List ───────────────────────────────────────
# list[start:stop]  → from 'start' up to BUT NOT including 'stop'

print("\n--- Slicing ---")
print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # [10, 20, 30]  — from beginning to index 3
print(numbers[2:])      # [30, 40, 50]  — from index 2 to the end
print(numbers[::-1])    # [50, 40, 30, 20, 10] — reversed!

# ── 4. MODIFYING LISTS ────────────────────────────────────────────────────
print("\n--- Modifying Lists ---")

# Adding items
fruits.append("date")           # Adds to the END
fruits.insert(1, "avocado")     # Inserts at a specific position
print("After add:", fruits)

# Removing items
fruits.remove("banana")         # Remove by VALUE (first match)
popped = fruits.pop()           # Remove & return the LAST item
print("After remove:", fruits)
print("Popped item:", popped)

# Updating an item
fruits[0] = "mango"             # Replace the item at index 0
print("After update:", fruits)

# ── 5. USEFUL LIST OPERATIONS ─────────────────────────────────────────────
scores = [45, 98, 73, 12, 88, 73]

print(f"\nLength:   {len(scores)}")         # 6
print(f"Sum:      {sum(scores)}")           # 389
print(f"Min:      {min(scores)}")           # 12
print(f"Max:      {max(scores)}")           # 98
print(f"Sorted:   {sorted(scores)}")        # [12, 45, 73, 73, 88, 98]
print(f"Count 73: {scores.count(73)}")      # 2 (how many times 73 appears)
print(f"73 at:    {scores.index(73)}")      # 2 (first position of 73)
print(f"98 in?:   {98 in scores}")          # True

# ── 6. LIST COMPREHENSIONS — Compact List Creation ────────────────────────
# Instead of writing a loop to build a list, you can do it in one line.
# Syntax: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n ** 2 for n in numbers]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]

print(f"\nSquares:       {squares}")
print(f"Even squares:  {even_squares}")


# ══════════════════════════════════════════════════════════════════════════
#  PART 2: DICTIONARIES
# ══════════════════════════════════════════════════════════════════════════

# ── 7. CREATING DICTIONARIES ──────────────────────────────────────────────
# Syntax: {key: value, key: value, ...}
# Keys must be unique. Values can be anything.

person = {
    "name": "Alice",
    "age": 30,
    "city": "London",
    "hobbies": ["reading", "cycling"]  # Values can be lists!
}

print("\n--- Dictionary ---")
print(person)

# ── 8. ACCESSING VALUES ───────────────────────────────────────────────────
print(person["name"])                   # Alice
print(person["hobbies"])                # ['reading', 'cycling']
print(person["hobbies"][0])             # reading (accessing list inside dict)

# .get() is safer — returns None (or a default) if key doesn't exist
print(person.get("email"))              # None (no crash!)
print(person.get("email", "N/A"))       # N/A (custom default)

# ── 9. MODIFYING DICTIONARIES ─────────────────────────────────────────────
person["age"] = 31                      # Update existing key
person["email"] = "alice@example.com"   # Add a new key

del person["city"]                      # Delete a key

print("\nUpdated person:", person)

# ── 10. LOOPING OVER DICTIONARIES ─────────────────────────────────────────
print("\n--- Looping ---")

# Keys only
for key in person:
    print(f"  Key: {key}")

# Keys and values
for key, value in person.items():
    print(f"  {key}: {value}")

# ── 11. USEFUL DICTIONARY METHODS ─────────────────────────────────────────
print("\n--- Dict Methods ---")
print("Keys:   ", list(person.keys()))
print("Values: ", list(person.values()))
print("Age in? ", "age" in person)      # True — checking if key exists

# ── 12. REAL-WORLD MINI PROJECT: Student Grade Tracker ────────────────────

def calculate_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)

def grade_letter(average):
    """Return a letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

students = {
    "Alice":  [88, 92, 79, 95],
    "Bob":    [65, 70, 58, 72],
    "Carlos": [91, 88, 94, 97],
    "Diana":  [55, 60, 52, 48],
}

print("\n--- 📊 Student Report ---")
print(f"{'Name':<10} {'Average':>8} {'Grade':>6}")
print("-" * 28)

for name, grades in students.items():
    avg = calculate_average(grades)
    grade = grade_letter(avg)
    print(f"{name:<10} {avg:>8.1f} {grade:>6}")

print("\n✅ Lesson 05 complete! Move on to exercises/ex_05_lists_and_dicts.py")
