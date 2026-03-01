"""
=============================================================
  SOLUTION 06: OOP Challenge — Library System
=============================================================
  Only look at this after attempting the exercises yourself!
=============================================================
"""


# ── TASK 1: Book Class ────────────────────────────────────

class Book:
    """Represents a library book."""

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


# ── TASK 2: Member Class ──────────────────────────────────

class Member:
    """A standard library member."""

    MAX_BOOKS = 3   # Class variable — shared by all standard members

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        """Borrow a book if it's available and within the limit."""
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            print(
                f"❌ {self.name} cannot borrow more books. "
                f"Limit of {self.MAX_BOOKS} reached."
            )
            return

        if not book.is_available:
            print(f"❌ '{book.title}' is not available right now.")
            return

        book.is_available = False
        self.borrowed_books.append(book)
        print(f"📗 {self.name} borrowed: {book.title}")

    def return_book(self, book):
        """Return a borrowed book."""
        if book not in self.borrowed_books:
            print(f"⚠️  {self.name} didn't borrow '{book.title}'.")
            return

        book.is_available = True
        self.borrowed_books.remove(book)
        print(f"✅ {self.name} returned: {book.title}")

    def __str__(self):
        count = len(self.borrowed_books)
        return f"{self.name} ({self.member_id}) — {count} book(s) borrowed"


# ── TASK 3: PremiumMember ─────────────────────────────────

class PremiumMember(Member):
    """A premium member with extended borrowing privileges."""

    MAX_BOOKS = 10                        # Overrides the class variable
    membership_tier = "Premium"

    def __str__(self):
        count = len(self.borrowed_books)
        return (
            f"⭐ {self.name} ({self.member_id}) "
            f"[{self.membership_tier}] — {count} book(s) borrowed"
        )


# ── TASK 4: Library Class ─────────────────────────────────

class Library:
    """Manages a collection of books and members."""

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def register_member(self, member):
        """Register a new library member."""
        self.members.append(member)
        print(f"🪪  Registered: {member.name}")

    def search_by_title(self, query):
        """Return books whose title contains the query (case-insensitive)."""
        query_lower = query.lower()
        return [b for b in self.books if query_lower in b.title.lower()]

    def search_by_author(self, author):
        """Return all books by the given author (case-insensitive)."""
        author_lower = author.lower()
        return [b for b in self.books if author_lower in b.author.lower()]

    def available_books(self):
        """Return all currently available books."""
        return [b for b in self.books if b.is_available]

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return (
            f"📚 {self.name} — "
            f"{len(self.books)} books, {len(self.members)} members"
        )


# ── TASK 5: Full System Test ──────────────────────────────
print("=" * 50)
print("  Library System — Full Test")
print("=" * 50)

# Create library
lib = Library("City Central Library")

# Add books
books = [
    Book("1984", "George Orwell", 1949, 328),
    Book("Animal Farm", "George Orwell", 1945, 112),
    Book("The Hobbit", "J.R.R. Tolkien", 1937, 310),
    Book("Dune", "Frank Herbert", 1965, 412),
    Book("Neuromancer", "William Gibson", 1984, 271),
]
for book in books:
    lib.add_book(book)

# Register members
print()
alice = Member("Alice", "M001")
bob   = PremiumMember("Bob", "M002")
lib.register_member(alice)
lib.register_member(bob)

print(f"\n{lib}")
print(f"Total books: {len(lib)}")

# Borrowing
print("\n--- Borrowing ---")
alice.borrow(books[0])   # 1984
alice.borrow(books[1])   # Animal Farm
alice.borrow(books[2])   # The Hobbit
alice.borrow(books[3])   # Should FAIL — Alice's limit is 3

bob.borrow(books[3])     # Dune — Bob is Premium, should succeed
bob.borrow(books[4])     # Neuromancer

print("\n--- Current Members ---")
print(alice)
print(bob)

# Returning
print("\n--- Returning ---")
alice.return_book(books[0])
print(alice)

# Searching
print("\n--- Search by Author: George Orwell ---")
results = lib.search_by_author("George Orwell")
for b in results:
    status = "✅ Available" if b.is_available else "❌ Checked out"
    print(f"  {b} — {status}")

print("\n--- Available Books ---")
for b in lib.available_books():
    print(f"  {b}")

print("\n🎉 Congratulations! You've built a working library system with OOP!")
