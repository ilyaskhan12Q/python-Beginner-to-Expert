"""
=============================================================
  EXERCISE 06: OOP Challenge — Build a Library System
  Based on: lessons/06 through 09
=============================================================

You will build a mini Library Management System using OOP.
This exercise combines everything you've learned.

Work through the tasks in order — each builds on the last.

Run your code often to test as you go:
    python exercises/ex_06_oop_challenge.py
=============================================================
"""

# ─────────────────────────────────────────────────────────
# TASK 1 (OOP Basics)
# Create a class called Book with:
#   Attributes:
#     - title (str)
#     - author (str)
#     - year (int)
#     - pages (int)
#     - is_available (bool) — starts as True
#
#   Methods:
#     - __str__: returns  "Title by Author (Year)"
#     - __repr__: returns  Book(title='...', author='...')
#
# Test it:
#   book = Book("1984", "George Orwell", 1949, 328)
#   print(book)   →  1984 by George Orwell (1949)
# ─────────────────────────────────────────────────────────

print("=== Task 1: Book Class ===")
# ↓ Write your Book class below


# ─────────────────────────────────────────────────────────
# TASK 2 (Methods & Logic)
# Create a class called Member with:
#   Attributes:
#     - name (str)
#     - member_id (str)
#     - borrowed_books (list) — starts empty
#     - MAX_BOOKS (class variable, = 3)
#
#   Methods:
#     - borrow(book):
#         If book is available AND member has < MAX_BOOKS:
#             Mark book as unavailable, add to borrowed_books,
#             print success message.
#         Otherwise print an appropriate error.
#
#     - return_book(book):
#         If book is in borrowed_books:
#             Mark book as available, remove from borrowed_books,
#             print success message.
#         Otherwise: print error message.
#
#     - __str__: returns "Name (ID) — N book(s) borrowed"
# ─────────────────────────────────────────────────────────

print("\n=== Task 2: Member Class ===")
# ↓ Write your Member class below


# ─────────────────────────────────────────────────────────
# TASK 3 (Inheritance)
# Create a class PremiumMember that INHERITS from Member.
# Premium members can borrow up to 10 books instead of 3.
# Add an attribute: membership_tier = "Premium"
# Override __str__ to show: "⭐ Name (ID) [Premium] — N book(s)"
# ─────────────────────────────────────────────────────────

print("\n=== Task 3: PremiumMember Class ===")
# ↓ Write your PremiumMember class below


# ─────────────────────────────────────────────────────────
# TASK 4 (Bringing it together)
# Create a Library class:
#   Attributes:
#     - name (str)
#     - books (list)
#     - members (list)
#
#   Methods:
#     - add_book(book)
#     - register_member(member)
#     - search_by_title(query) → returns list of matching books
#     - search_by_author(author) → returns list of matching books
#     - available_books() → returns list of available books
#     - __len__: returns total number of books
#     - __str__: returns "Library Name — N books, M members"
# ─────────────────────────────────────────────────────────

print("\n=== Task 4: Library Class ===")
# ↓ Write your Library class below


# ─────────────────────────────────────────────────────────
# TASK 5 (Test Everything!)
# Use your classes to run this script and see the output.
# ─────────────────────────────────────────────────────────

print("\n=== Task 5: Full System Test ===")

# Uncomment and run this once you've built your classes above:

# # Create a library
# lib = Library("City Central Library")

# # Add books
# books = [
#     Book("1984", "George Orwell", 1949, 328),
#     Book("Animal Farm", "George Orwell", 1945, 112),
#     Book("The Hobbit", "J.R.R. Tolkien", 1937, 310),
#     Book("Dune", "Frank Herbert", 1965, 412),
#     Book("Neuromancer", "William Gibson", 1984, 271),
# ]
# for book in books:
#     lib.add_book(book)

# # Register members
# alice = Member("Alice", "M001")
# bob   = PremiumMember("Bob", "M002")
# lib.register_member(alice)
# lib.register_member(bob)

# print(lib)
# print(f"Total books: {len(lib)}")

# # Borrowing
# print("\n--- Borrowing ---")
# alice.borrow(books[0])
# alice.borrow(books[1])
# alice.borrow(books[2])
# alice.borrow(books[3])   # Should fail — limit reached

# bob.borrow(books[3])     # Premium — should succeed
# bob.borrow(books[4])

# print("\n--- Current Members ---")
# print(alice)
# print(bob)

# # Returning
# print("\n--- Returning ---")
# alice.return_book(books[0])
# print(alice)

# # Searching
# print("\n--- Search by Author: George Orwell ---")
# results = lib.search_by_author("George Orwell")
# for b in results:
#     status = "✅ Available" if b.is_available else "❌ Checked out"
#     print(f"  {b} — {status}")

# print("\n--- Available Books ---")
# for b in lib.available_books():
#     print(f"  {b}")

print("\n✅ Complete! Check solutions/sol_06_oop_challenge.py when ready.")
