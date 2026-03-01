"""
=============================================================
  LESSON 06: Introduction to OOP — Why & What
=============================================================

REAL-WORLD ANALOGY:
  Imagine you're building a video game with 100 different characters.
  Each character has:  name, health, attack_power
  Each character can:  attack, defend, heal

  WITHOUT OOP — you'd write 100 × 3 = 300 variables
                and 100 × 3 = 300 separate functions. 😱

  WITH OOP    — you write ONE blueprint (class) called Character.
                Then you create 100 characters from it.
                Each has its own name/health/power, but
                they ALL share the same behaviors. ✅

  That blueprint is called a CLASS.
  Each character created from it is called an OBJECT (or instance).
=============================================================
"""

# ── THE PROBLEM WITHOUT OOP ───────────────────────────────────────────────
# Let's see what managing multiple "things" looks like without OOP.

print("=== Without OOP ===")

# Character 1 — lots of individual variables
char1_name = "Aragorn"
char1_health = 100
char1_attack = 25

# Character 2 — same pattern, repeated
char2_name = "Legolas"
char2_health = 90
char2_attack = 30

# A function to attack — must receive data as arguments
def character_attack(attacker_name, attacker_attack, target_name, target_health):
    """Simulate one character attacking another."""
    new_health = target_health - attacker_attack
    print(f"{attacker_name} attacks {target_name} for {attacker_attack} damage!")
    print(f"{target_name}'s health: {target_health} → {new_health}")
    return new_health  # Must return and re-assign manually

char2_health = character_attack(char1_name, char1_attack, char2_name, char2_health)

# Problems with this approach:
# 1. Every new character = many more variables.
# 2. Functions are disconnected from the data they work on.
# 3. It's hard to keep track of who owns which variable.
# 4. Adding a new feature (e.g., "level") means updating EVERYTHING.

print("\n--- Imagine doing this for 50 characters... 😰 ---\n")


# ── THE SOLUTION WITH OOP ─────────────────────────────────────────────────
# Now let's solve the same problem with a class.
# The class bundles the DATA (attributes) and BEHAVIOR (methods) together.

print("=== With OOP ===\n")

class Character:
    """
    A blueprint for a game character.

    Think of this class as a template or cookie cutter.
    Every character created from it is a separate, independent cookie —
    same shape, different toppings (data).
    """

    # The __init__ method runs automatically when you create a new object.
    # 'self' refers to the specific object being created.
    def __init__(self, name, health, attack_power):
        self.name = name               # Each object gets its OWN name
        self.health = health           # ...its OWN health
        self.attack_power = attack_power  # ...its OWN attack power

    # Methods = functions that belong to the class
    # They always receive 'self' as the first argument.
    def attack(self, target):
        """Attack another character."""
        target.health -= self.attack_power
        print(f"⚔️  {self.name} attacks {target.name} for {self.attack_power} damage!")
        print(f"   {target.name}'s health: {target.health}")

    def heal(self, amount):
        """Recover some health."""
        self.health += amount
        print(f"💚 {self.name} heals for {amount}. Health: {self.health}")

    def is_alive(self):
        """Return True if the character is still alive."""
        return self.health > 0

    def status(self):
        """Print the character's current status."""
        alive = "Alive ✅" if self.is_alive() else "Defeated ❌"
        print(f"🧑 {self.name:12} | HP: {self.health:>4} | ATK: {self.attack_power} | {alive}")


# Creating OBJECTS from the class (instantiation)
aragorn = Character("Aragorn", 100, 25)
legolas = Character("Legolas", 90, 30)
gimli   = Character("Gimli",   120, 20)

print("Initial status:")
aragorn.status()
legolas.status()
gimli.status()

print()
aragorn.attack(legolas)      # Aragorn attacks Legolas
print()
legolas.attack(aragorn)      # Legolas attacks back
legolas.heal(15)             # Legolas heals

print()
print("Final status:")
aragorn.status()
legolas.status()

# ── KEY OOP CONCEPTS INTRODUCED ───────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════╗
║              OOP Vocabulary So Far                   ║
╠══════════════════════════════════════════════════════╣
║  CLASS      The blueprint/template (Character)       ║
║  OBJECT     One item made from the blueprint         ║
║             (aragorn, legolas, gimli)                ║
║  ATTRIBUTE  Data stored ON the object                ║
║             (self.name, self.health)                 ║
║  METHOD     A function that belongs to the class     ║
║             (attack, heal, status)                   ║
║  SELF       The object itself — connects data        ║
║             and methods to the right instance        ║
╚══════════════════════════════════════════════════════╝
""")

print("✅ Lesson 06 complete! Continue to lessons/07_classes_and_objects.py")
