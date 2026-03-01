"""
=============================================================
  LESSON 08: Inheritance — Building on What Exists
=============================================================

REAL-WORLD ANALOGY:
  Think of animals:
    All animals can breathe and move.
    Dogs can do those things AND bark.
    Birds can do those things AND fly.

  Instead of rewriting "breathe" and "move" for every animal,
  we write it ONCE in a base Animal class, and Dog/Bird
  INHERIT those abilities automatically.

  Inheritance = "is a" relationship
    A Dog IS AN Animal.
    A SavingsAccount IS A BankAccount.
    A Manager IS AN Employee.
=============================================================
"""


# ── 1. BASE CLASS (Parent Class) ──────────────────────────────────────────
# This is the class that others will inherit from.

class Animal:
    """Base class for all animals."""

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_alive = True

    def breathe(self):
        print(f"{self.name} inhales... exhales...")

    def eat(self, food):
        print(f"{self.name} eats {food}. 😋")

    def sleep(self):
        print(f"{self.name} is sleeping. 💤")

    def __str__(self):
        return f"{self.species} named {self.name} (age {self.age})"


# ── 2. CHILD CLASSES (Subclasses) ─────────────────────────────────────────
# A child class INHERITS everything from the parent.
# It can also ADD new methods or OVERRIDE existing ones.

class Dog(Animal):  # Dog inherits from Animal
    """A dog — an Animal with dog-specific behaviours."""

    def __init__(self, name, age, breed):
        # super() calls the parent's __init__ — reuses its setup code.
        # We don't need to repeat self.name, self.is_alive, etc.
        super().__init__(name, species="Dog", age=age)
        self.breed = breed            # Dog-specific attribute
        self.tricks = []              # Dogs can learn tricks!

    def bark(self):
        """Dogs can bark. Animals in general cannot."""
        print(f"🐕 {self.name} says: Woof! Woof!")

    def learn_trick(self, trick):
        """Teach the dog a new trick."""
        self.tricks.append(trick)
        print(f"🎓 {self.name} learned: {trick}!")

    def perform(self):
        """Show off all known tricks."""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
            return
        print(f"✨ {self.name}'s tricks: {', '.join(self.tricks)}")

    # OVERRIDING a parent method — we keep the same name, change the behaviour
    def eat(self, food):
        """Dogs eat enthusiastically!"""
        super().eat(food)           # Call the parent's version first
        print(f"   (gobbles it up in 3 seconds)")


class Cat(Animal):  # Cat inherits from Animal
    """A cat — independent and a little aloof."""

    def __init__(self, name, age, indoor=True):
        super().__init__(name, species="Cat", age=age)
        self.indoor = indoor
        self.mood = "content"

    def meow(self):
        print(f"🐈 {self.name} says: Meow~")

    def purr(self):
        print(f"🐈 {self.name} purrs contentedly...")

    # Overriding eat with very different cat behaviour
    def eat(self, food):
        print(f"{self.name} sniffs the {food}...")
        print(f"   ...decides it's acceptable. Eats half of it.")
        print(f"   ...ignores the rest.")


class Bird(Animal):
    """A bird — lightweight and airborne."""

    def __init__(self, name, age, can_fly=True):
        super().__init__(name, species="Bird", age=age)
        self.can_fly = can_fly

    def chirp(self):
        print(f"🐦 {self.name} chirps melodically!")

    def fly(self):
        if self.can_fly:
            print(f"🦅 {self.name} spreads its wings and soars!")
        else:
            print(f"😢 {self.name} can't fly — but it can run!")


# ── 3. USING INHERITANCE ──────────────────────────────────────────────────
print("=== Animal Kingdom Demo ===\n")

rex  = Dog("Rex", age=4, breed="German Shepherd")
luna = Cat("Luna", age=3, indoor=True)
tweety = Bird("Tweety", age=2)

print(rex)      # Uses Animal's __str__
print(luna)
print(tweety)

print("\n--- Rex the Dog ---")
rex.breathe()              # Inherited from Animal
rex.bark()                 # Dog-specific
rex.eat("steak")           # Overridden Dog version
rex.learn_trick("sit")
rex.learn_trick("roll over")
rex.perform()

print("\n--- Luna the Cat ---")
luna.meow()
luna.eat("fancy tuna")     # Overridden Cat version
luna.sleep()               # Inherited from Animal

print("\n--- Tweety the Bird ---")
tweety.chirp()
tweety.fly()


# ── 4. isinstance() — Checking Relationships ──────────────────────────────
print("\n--- Type Checking ---")
print(f"Is Rex a Dog?    {isinstance(rex, Dog)}")      # True
print(f"Is Rex an Animal?{isinstance(rex, Animal)}")   # True! Dogs ARE animals
print(f"Is Rex a Cat?    {isinstance(rex, Cat)}")      # False

print(f"\nIs Luna a Cat?   {isinstance(luna, Cat)}")   # True
print(f"Is Luna a Dog?   {isinstance(luna, Dog)}")     # False


# ── 5. MULTI-LEVEL INHERITANCE ────────────────────────────────────────────
# A class can inherit from a class that itself inherits from another.

class GuideDog(Dog):   # GuideDog → Dog → Animal
    """A trained guide dog for visually impaired people."""

    def __init__(self, name, age, breed, owner_name):
        super().__init__(name, age, breed)
        self.owner_name = owner_name
        self.is_on_duty = False

    def guide(self):
        print(f"🦮 {self.name} is guiding {self.owner_name} safely.")

    def go_on_duty(self):
        self.is_on_duty = True
        print(f"{self.name} is now on duty. Please do not pet! 🚫")

    def go_off_duty(self):
        self.is_on_duty = False
        print(f"{self.name} is off duty. Pets are welcome! 🐾")


buddy = GuideDog("Buddy", age=5, breed="Labrador", owner_name="James")
print("\n--- Guide Dog Demo ---")
buddy.go_on_duty()
buddy.guide()
buddy.bark()          # Still a Dog — can still bark
buddy.breathe()       # Still an Animal — can breathe
buddy.go_off_duty()
buddy.perform()       # No tricks yet


# ── 6. POLYMORPHISM — One Interface, Many Behaviours ──────────────────────
# Because all animals have an eat() method, we can call it
# on ANY animal without knowing its exact type.
# Each animal will behave differently — that's POLYMORPHISM.

print("\n--- Polymorphism: Feeding all animals ---")
animals = [rex, luna, tweety]

for animal in animals:
    print(f"\nFeeding {animal.name}:")
    animal.eat("dinner")   # Each one behaves differently!

print("\n✅ Lesson 08 complete! Continue to lessons/09_encapsulation_and_magic.py")
