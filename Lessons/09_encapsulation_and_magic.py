"""
=============================================================
  LESSON 09: Encapsulation & Magic Methods
=============================================================

REAL-WORLD ANALOGY:
  ENCAPSULATION:
    Your bank account has a balance — but the bank doesn't
    let you edit it directly. You must use deposit() or
    withdraw(). The balance is PROTECTED. The interface
    (deposit/withdraw) is CONTROLLED. That's encapsulation.

  MAGIC METHODS (dunder methods):
    Python has special methods like __str__, __len__,
    __add__ that control how your objects behave with
    built-in Python operations (print, len, +, ==, etc.)
    They have double underscores — hence "dunder" (double under).
=============================================================
"""


# ══════════════════════════════════════════════════════════════════════════
#  PART 1: ENCAPSULATION
# ══════════════════════════════════════════════════════════════════════════

class Temperature:
    """
    A temperature value with enforced validation.

    Demonstrates encapsulation using properties.
    Internally stores Celsius. Can report in Fahrenheit too.
    """

    ABSOLUTE_ZERO = -273.15  # Kelvin → Celsius conversion

    def __init__(self, celsius=0.0):
        # We use the PROPERTY setter from the start — enforces validation.
        self.celsius = celsius   # Calls the setter below

    # ── PROPERTY: Controlled access to _celsius ───────────────────────────
    # @property turns a method into an "attribute".
    # Reading  self.celsius calls the getter.
    # Writing  self.celsius = x  calls the setter.

    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius   # _celsius is the "private" internal variable

    @celsius.setter
    def celsius(self, value):
        """Set temperature — rejects values below absolute zero."""
        if value < Temperature.ABSOLUTE_ZERO:
            raise ValueError(
                f"Temperature {value}°C is below absolute zero "
                f"({Temperature.ABSOLUTE_ZERO}°C)!"
            )
        self._celsius = value

    @property
    def fahrenheit(self):
        """Derived property — always calculated from Celsius."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Allow setting temperature via Fahrenheit."""
        self.celsius = (value - 32) * 5 / 9   # Converts and validates

    @property
    def kelvin(self):
        """Temperature in Kelvin."""
        return self._celsius - Temperature.ABSOLUTE_ZERO

    def __str__(self):
        return (
            f"{self._celsius:.1f}°C / "
            f"{self.fahrenheit:.1f}°F / "
            f"{self.kelvin:.1f}K"
        )


# Testing Temperature
print("=== Temperature ===")
boiling = Temperature(100)
print(f"Boiling point: {boiling}")

freezing = Temperature(0)
print(f"Freezing point: {freezing}")

body = Temperature()
body.fahrenheit = 98.6    # Set via Fahrenheit, stored as Celsius
print(f"Body temperature: {body}")

# Validation in action
print("\nTrying to set an impossible temperature...")
try:
    impossible = Temperature(-300)
except ValueError as e:
    print(f"❌ Error caught: {e}")


# ══════════════════════════════════════════════════════════════════════════
#  PART 2: MAGIC METHODS (Dunder Methods)
# ══════════════════════════════════════════════════════════════════════════

class Vector:
    """
    A 2D mathematical vector — great for teaching magic methods.
    A vector is just a direction and magnitude: (x, y)
    e.g., "3 steps right and 4 steps up" → Vector(3, 4)
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ── __str__ — controls print(object) ─────────────────────────────────
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # ── __repr__ — controls how it looks in the Python shell ─────────────
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    # ── __len__ — controls len(object) ───────────────────────────────────
    # We'll return magnitude as integer (not strictly math, but illustrative)
    def __len__(self):
        import math
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # ── __add__ — controls a + b ──────────────────────────────────────────
    def __add__(self, other):
        """Add two vectors: (1,2) + (3,4) = (4,6)"""
        return Vector(self.x + other.x, self.y + other.y)

    # ── __sub__ — controls a - b ──────────────────────────────────────────
    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    # ── __mul__ — controls a * b ──────────────────────────────────────────
    def __mul__(self, scalar):
        """Scale a vector by a number: Vector(2,3) * 2 = Vector(4,6)"""
        return Vector(self.x * scalar, self.y * scalar)

    # ── __eq__ — controls a == b ──────────────────────────────────────────
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # ── __abs__ — controls abs(object) ───────────────────────────────────
    def __abs__(self):
        """Return the magnitude (length) of the vector."""
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # ── __neg__ — controls -object ────────────────────────────────────────
    def __neg__(self):
        return Vector(-self.x, -self.y)

    # ── __bool__ — controls bool(object) / truthiness ────────────────────
    def __bool__(self):
        """A zero vector (0, 0) is falsy."""
        return self.x != 0 or self.y != 0


# Testing Vector with magic methods
print("\n=== Vector Magic Methods ===")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

print(f"\nv1 + v2 = {v1 + v2}")       # __add__
print(f"v1 - v2 = {v1 - v2}")       # __sub__
print(f"v1 * 3  = {v1 * 3}")        # __mul__
print(f"-v1     = {-v1}")           # __neg__
print(f"v1 == v2: {v1 == v2}")      # __eq__
print(f"|v1|    = {abs(v1):.2f}")   # __abs__ (magnitude)
print(f"len(v1) = {len(v1)}")       # __len__
print(f"bool(v1): {bool(v1)}")      # __bool__

zero_vector = Vector(0, 0)
print(f"bool(Vector(0,0)): {bool(zero_vector)}")  # False


# ── BRINGING IT TOGETHER: A ShoppingCart class ────────────────────────────

class CartItem:
    """A single item in a shopping cart."""

    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} x{self.quantity} @ £{self.price:.2f} = £{self.subtotal:.2f}"


class ShoppingCart:
    """A shopping cart with magic method support."""

    def __init__(self):
        self._items = []

    def add(self, item):
        """Add a CartItem to the cart."""
        self._items.append(item)

    def __len__(self):
        """len(cart) returns number of ITEMS (not unique products)."""
        return sum(item.quantity for item in self._items)

    def __str__(self):
        if not self._items:
            return "🛒 Your cart is empty."
        lines = ["🛒 Shopping Cart:", "─" * 40]
        for item in self._items:
            lines.append(f"   {item}")
        lines.append("─" * 40)
        lines.append(f"   TOTAL: £{self.total:.2f}")
        return "\n".join(lines)

    def __bool__(self):
        """An empty cart is falsy."""
        return len(self._items) > 0

    def __iter__(self):
        """Allows: for item in cart"""
        return iter(self._items)

    @property
    def total(self):
        return sum(item.subtotal for item in self._items)


# Demo
print("\n=== Shopping Cart Demo ===")
cart = ShoppingCart()

print(f"Empty cart? {not bool(cart)}")  # True

cart.add(CartItem("Python Book", 29.99))
cart.add(CartItem("Mechanical Keyboard", 89.99, quantity=1))
cart.add(CartItem("USB-C Cable", 9.99, quantity=3))

print(cart)
print(f"\nTotal items in cart: {len(cart)}")

print("\nLooping over cart items:")
for item in cart:
    print(f"  → {item.name}: £{item.subtotal:.2f}")

print("\n✅ Lesson 09 complete! You've finished the core curriculum! 🎉")
print("   Head to exercises/ex_06_oop_challenge.py for your final challenge.")
