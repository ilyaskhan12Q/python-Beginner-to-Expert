"""
=============================================================
  LESSON 07: Classes & Objects — Deep Dive
=============================================================

REAL-WORLD ANALOGY:
  A CLASS is the architectural blueprint for a house.
  An OBJECT is the actual house built from that blueprint.

  One blueprint → many different houses.
  Same structure, different addresses & paint colors.
=============================================================
"""


# ── 1. A WELL-STRUCTURED CLASS ────────────────────────────────────────────

class BankAccount:
    """
    Represents a bank account.

    Attributes:
        owner (str):   The name of the account holder.
        balance (float): The current balance in the account.
    """

    # Class variable — shared by ALL instances of BankAccount.
    # This is the SAME value for every account object.
    interest_rate = 0.03    # 3% annual interest

    def __init__(self, owner, initial_deposit=0.0):
        """
        Initialise a new bank account.

        Args:
            owner (str):             Name of the account owner.
            initial_deposit (float): Starting balance (default 0).
        """
        # Instance variables — unique to EACH object
        self.owner = owner
        self.balance = float(initial_deposit)
        self._transactions = []   # Leading _ = "intended as private"

    # ── INSTANCE METHODS ──────────────────────────────────────────────────

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("⚠️  Deposit amount must be positive.")
            return
        self.balance += amount
        self._transactions.append(f"+ £{amount:.2f}")
        print(f"✅ Deposited £{amount:.2f}. New balance: £{self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw money. Refuses if funds are insufficient."""
        if amount <= 0:
            print("⚠️  Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"❌ Insufficient funds. Balance: £{self.balance:.2f}")
            return
        self.balance -= amount
        self._transactions.append(f"- £{amount:.2f}")
        print(f"💸 Withdrew £{amount:.2f}. New balance: £{self.balance:.2f}")

    def apply_interest(self):
        """Apply annual interest to the account balance."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        self._transactions.append(f"~ Interest +£{interest:.2f}")
        print(f"📈 Interest applied: +£{interest:.2f}. Balance: £{self.balance:.2f}")

    def print_statement(self):
        """Print a formatted account statement."""
        print(f"\n{'─' * 35}")
        print(f"  Account: {self.owner}")
        print(f"{'─' * 35}")
        if not self._transactions:
            print("  No transactions yet.")
        for t in self._transactions:
            print(f"  {t}")
        print(f"{'─' * 35}")
        print(f"  Current Balance: £{self.balance:.2f}")
        print(f"{'─' * 35}")

    # ── CLASS METHOD ──────────────────────────────────────────────────────
    # A class method works on the CLASS itself, not a specific object.
    # Useful for factory patterns (alternative constructors).

    @classmethod
    def create_savings_account(cls, owner):
        """Factory: create a savings account with a £500 bonus."""
        print(f"🎁 Creating savings account for {owner} with £500 bonus!")
        return cls(owner, initial_deposit=500.0)   # cls = BankAccount here

    # ── STATIC METHOD ─────────────────────────────────────────────────────
    # A static method is a plain function that lives in the class namespace.
    # It doesn't use 'self' or 'cls'. It's just logically grouped here.

    @staticmethod
    def is_valid_amount(amount):
        """Check if an amount is a valid positive number."""
        return isinstance(amount, (int, float)) and amount > 0

    # ── SPECIAL METHOD: __str__ ───────────────────────────────────────────
    # Controls what print(object) displays.

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance=£{self.balance:.2f})"


# ── 2. USING THE CLASS ────────────────────────────────────────────────────

print("=== BankAccount Demo ===\n")

# Creating objects
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob")              # No initial deposit → defaults to 0

print(alice_account)    # Uses __str__
print(bob_account)

print("\n--- Alice's transactions ---")
alice_account.deposit(500)
alice_account.withdraw(200)
alice_account.withdraw(1500)   # Should fail
alice_account.apply_interest()
alice_account.print_statement()

print("\n--- Bob's transactions ---")
bob_account.deposit(250)
bob_account.print_statement()

# Class method usage
print("\n--- Savings Account (Class Method) ---")
savings = BankAccount.create_savings_account("Carlos")
print(savings)

# Static method usage
print("\n--- Static Method ---")
print(BankAccount.is_valid_amount(100))     # True
print(BankAccount.is_valid_amount(-50))     # False
print(BankAccount.is_valid_amount("abc"))   # False

# Accessing class variable
print(f"\nInterest rate: {BankAccount.interest_rate * 100}%")


# ── 3. THE MAGIC OF self ──────────────────────────────────────────────────
print("""
┌──────────────────────────────────────────────────────┐
│  What is 'self'?                                     │
│                                                      │
│  When you write alice_account.deposit(500):          │
│  Python secretly turns it into:                      │
│  BankAccount.deposit(alice_account, 500)             │
│                                                      │
│  'self' is Python passing the object itself          │
│  as the first argument automatically.                │
│                                                      │
│  It's how methods know WHICH object's data to use.  │
└──────────────────────────────────────────────────────┘
""")

print("✅ Lesson 07 complete! Continue to lessons/08_inheritance.py")
