# 🤝 Contributing to Python: Zero to OOP Hero

First off — **thank you** for being here. Whether you're fixing a typo, adding an exercise, or writing a whole new lesson, your contribution matters. This project exists to help beginners, and every improvement brings more people into programming.

---

## 📋 Table of Contents

1. [Code of Conduct](#-code-of-conduct)
2. [Ways to Contribute](#-ways-to-contribute)
3. [Before You Start](#-before-you-start)
4. [Development Setup](#-development-setup)
5. [Contribution Workflow](#-contribution-workflow)
6. [Writing Standards](#-writing-standards)
7. [Lesson Format Guide](#-lesson-format-guide)
8. [Exercise Format Guide](#-exercise-format-guide)
9. [Commit Message Style](#-commit-message-style)
10. [Pull Request Checklist](#-pull-request-checklist)
11. [Review Process](#-review-process)
12. [Badges & Recognition](#-badges--recognition)
13. [Getting Help](#-getting-help)

---

## 🌟 Code of Conduct

This project follows a simple rule:

> **Be kind. Everyone here is learning.**

Specifically:
- Welcome beginners. Never make someone feel stupid for asking a question.
- Give constructive feedback — point to what can improve, not just what's wrong.
- Respect different skill levels, backgrounds, and learning styles.
- No harassment, discrimination, or gatekeeping of any kind.

Violations can be reported by opening a private issue or emailing the maintainers directly.

---

## 🛠 Ways to Contribute

You don't need to write code to contribute. Here's the full range:

| Type | Examples | Difficulty |
|---|---|---|
| 🐛 **Bug fix** | Broken code, incorrect output, typo | Easy |
| 📖 **Docs improvement** | Clearer explanation, better analogy | Easy |
| ✍️ **New exercise** | Add tasks to an existing exercise file | Medium |
| 🎓 **New lesson** | Write a full lesson following our format | Medium–Hard |
| 💡 **Suggestion** | Open an issue with an idea | Zero code needed |
| 🌍 **Translation** | Translate lessons to another language | Medium |
| 🔍 **Review** | Review open PRs, spot issues | Any level |

---

## 🔧 Before You Start

### Check existing issues first

Before opening a new issue or starting work, **search open issues** to make sure no one is already working on the same thing. If there's an existing issue, leave a comment saying you'd like to work on it.

### For significant changes

If you want to add a new lesson or make a substantial change, **open an issue first** and describe what you're planning. This prevents wasted effort if the idea doesn't fit the project's direction.

---

## 💻 Development Setup

### Requirements

- Python 3.10 or higher
- Git
- A text editor (VS Code recommended)

### Steps

```bash
# 1. Fork the repo on GitHub (click the Fork button)

# 2. Clone YOUR fork
git clone https://github.com/YOUR-USERNAME/python-Beginner-Friendly.git
cd python-Beginner-Friendly

# 3. Verify Python version
python --version   # Must be 3.10+

# 4. Test that existing lessons run
python lessons/01_variables.py
python lessons/06_intro_to_oop.py

# 5. Add the upstream remote (so you can pull in future updates)
git remote add upstream https://github.com/ORIGINAL-OWNER/python-Beginner-Friendly.git
```

---

## 🔄 Contribution Workflow

```
fork → branch → edit → test → commit → push → pull request
```

### Step by step

```bash
# 1. Make sure your main branch is up to date
git checkout main
git pull upstream main

# 2. Create a branch named after what you're doing
#    Pattern: type/short-description
git checkout -b fix/typo-in-lesson-03
git checkout -b lesson/add-decorators
git checkout -b exercise/add-dict-challenge

# 3. Make your changes

# 4. Test EVERY file you touched
python lessons/03_control_flow.py
python exercises/ex_03_control_flow.py

# 5. Commit your changes (see commit style below)
git add .
git commit -m "fix: correct loop range in lesson 03 example"

# 6. Push to your fork
git push origin fix/typo-in-lesson-03

# 7. Open a Pull Request on GitHub
#    → Compare & pull request → fill in the PR template
```

---

## ✍️ Writing Standards

### Python code

All Python files must follow **PEP 8**. Key rules:

```python
# ✅ DO: snake_case for variables and functions
player_score = 0
def calculate_average(values):

# ❌ DON'T: camelCase or PascalCase for variables/functions
playerScore = 0
def CalculateAverage(values):

# ✅ DO: 4 spaces for indentation (never tabs)
def greet(name):
    print(f"Hello, {name}")

# ✅ DO: spaces around operators
x = a + b
result = value * 2

# ❌ DON'T: spaces missing or inconsistent
x=a+b

# ✅ DO: blank line between functions and classes
def first():
    pass


def second():
    pass

# ✅ DO: max line length of 88 characters
# ✅ DO: trailing newline at end of file

# ✅ DO: type hints for function signatures (Python 3.10+ style)
def add(a: int, b: int) -> int:
    return a + b

# ✅ DO: docstrings on every function and class
def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0
```

### Comments

Comments in lessons are **teaching tools** — they should explain the *why*, not restate the *what*:

```python
# ❌ BAD comment — just restates the code
x = x + 1  # Add 1 to x

# ✅ GOOD comment — explains purpose or a non-obvious choice
x += 1  # Increment the step counter before the next iteration

# ✅ Section dividers help navigation in long files
# ── PART 2: WORKING WITH DICTIONARIES ─────────────────────────
```

### Language and tone

- Write as if explaining to a friend who is smart but new to programming.
- Use **real-world analogies** before introducing new concepts.
- Short sentences. No jargon without explanation.
- British or American English both accepted — be consistent within a file.
- Avoid condescension. Never say "obviously" or "just".

---

## 📚 Lesson Format Guide

Every lesson file must follow this structure:

```python
"""
=============================================================
  LESSON XX: Title — Subtitle
=============================================================

REAL-WORLD ANALOGY:
  Your analogy here. Make it vivid and concrete.
  2–4 lines maximum.
=============================================================
"""

# ── 1. FIRST CONCEPT ──────────────────────────────────────────────────────
# One-line explanation of what this section covers.

<working code>

# ── 2. SECOND CONCEPT ─────────────────────────────────────────────────────
# ...

# ── N. MINI PROJECT / PUTTING IT TOGETHER ─────────────────────────────────
# A short, runnable program that combines the lesson's concepts.
# This should be satisfying to run and produce visible output.

print("\n✅ Lesson XX complete! Move on to exercises/ex_XX_topic.py")
```

**Lesson requirements checklist:**

- [ ] Opens with the standardised header block and analogy
- [ ] Uses `# ── SECTION NAME ───...` dividers (exactly as shown)
- [ ] Every section has a brief comment explaining the concept
- [ ] All code is runnable without modification
- [ ] Ends with a mini project that ties concepts together
- [ ] Ends with the `✅ Lesson XX complete!` print
- [ ] No external dependencies (standard library only)
- [ ] File uses `input()` sparingly and only at the end

---

## 🧩 Exercise Format Guide

```python
"""
=============================================================
  EXERCISE XX: Topic
  Based on: lessons/XX_topic.py
=============================================================

Instructions:
  [Brief instructions for the student]
=============================================================
"""

print("=" * 50)
print("  EXERCISE XX: Topic Name")
print("=" * 50)

# ─────────────────────────────────────────────────────────
# TASK 1 (Beginner)
# Clear description of what to do.
# Include the expected output as a comment.
# ─────────────────────────────────────────────────────────

print("\n--- Task 1: Task Name ---")
# ↓ Write your code below this line


# ─────────────────────────────────────────────────────────
# TASK 2 (Intermediate)
# ...
# ─────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────
# TASK 3 (Challenge)
# A harder version. Pushes the student beyond the lesson.
# ─────────────────────────────────────────────────────────

print("\n✅ All tasks done? Check solutions/sol_XX_topic.py")
```

**Exercise requirements checklist:**

- [ ] Minimum 3 tasks with increasing difficulty
- [ ] Difficulty labels: `(Beginner)`, `(Intermediate)`, `(Challenge)`
- [ ] Expected output shown in comments
- [ ] Placeholder comment `# ↓ Write your code below this line`
- [ ] No pre-filled solutions in the exercise file
- [ ] Matching solution file in `solutions/sol_XX_topic.py`

---

## 💬 Commit Message Style

Follow the [Conventional Commits](https://www.conventionalcommits.org/) standard:

```
<type>: <short description in present tense, lowercase>
```

| Type | When to use |
|---|---|
| `feat` | Adding a new lesson, exercise, or feature |
| `fix` | Fixing a bug, broken code, or incorrect output |
| `docs` | README, comments, docstrings, CONTRIBUTING updates |
| `style` | Formatting, whitespace — no logic change |
| `refactor` | Restructuring code without changing behaviour |
| `test` | Adding or fixing tests |
| `chore` | Maintenance tasks (CI, config, deps) |

**Examples:**

```bash
# ✅ Good
git commit -m "feat: add lesson 10 on file handling"
git commit -m "fix: correct off-by-one error in exercise 03 task 2"
git commit -m "docs: improve analogy in lesson 06 intro"
git commit -m "style: apply PEP8 formatting to lesson 04"

# ❌ Bad
git commit -m "update"
git commit -m "fixed stuff"
git commit -m "WIP"
git commit -m "lesson"
```

---

## ✅ Pull Request Checklist

Before submitting, confirm ALL of the following:

**Code quality**
- [ ] All modified Python files run without errors
- [ ] Code follows PEP 8 (check with `python -m pyflakes yourfile.py` or `flake8`)
- [ ] No debug `print()` statements left in
- [ ] No hardcoded paths or system-specific code

**Content quality**
- [ ] Lesson/exercise follows the format guides above
- [ ] Comments and docstrings are present and helpful
- [ ] Real-world analogies are included for new concepts
- [ ] If an exercise was added, a matching solution file exists

**PR hygiene**
- [ ] Branch name follows `type/description` convention
- [ ] Commits follow Conventional Commits format
- [ ] PR title is clear and descriptive
- [ ] PR description explains what changed and why
- [ ] If fixing a bug: steps to reproduce are included
- [ ] If adding content: screenshots or sample output included

---

## 🔍 Review Process

1. **Automated checks** run immediately when you open a PR.
2. A maintainer will review within **5 business days**.
3. You may receive change requests — this is normal and not a rejection.
4. Once approved, a maintainer will merge your PR.
5. **Your name will be added to the Contributors section** in the README.

### What reviewers look for

- Does the code run? Does it produce the expected output?
- Is it beginner-friendly? Could a total novice understand it?
- Does it follow the format and style guides?
- Is it adding genuine value, or duplicating existing content?

### What reviewers won't reject for

- Imperfect English (we'll fix it together)
- Less-than-perfect code style (we'll suggest fixes)
- First-time contributors making rookie mistakes (we've all been there)

---

## 🏅 Badges & Recognition

Contributing earns you badges you can display on your GitHub profile or in your README.

| Badge | How to Earn |
|---|---|
| 🚀 **First PR** | Your first merged pull request |
| 🐛 **Bug Hunter** | Report or fix a confirmed bug |
| 🤝 **Contributor** | Any merged PR |
| ✍️ **Lesson Author** | Write and merge a new lesson or exercise |
| 🏆 **OOP Master** | Complete all OOP lessons + contribute back |

See [.github/BADGE_GALLERY.html](./.github/BADGE_GALLERY.html) for the visual gallery and copy-paste Markdown for each badge.

**To claim your badge:** Comment on your merged PR with `@maintainer claim badge: <badge name>` and we'll send you the Markdown snippet.

---

## 🆘 Getting Help

Stuck? Not sure if your idea fits? Something not working?

- **Open a Discussion** for questions and ideas
- **Open an Issue** for bugs or content proposals
- **Tag `@maintainers`** in your PR if you need a review nudge

No question is too small. The whole point of this project is learning — and that includes learning to contribute to open source.

---

## 🎉 Thank You

Seriously. Open-source education projects like this one only exist because people choose to spend their time helping strangers learn. That's remarkable.

Every PR — no matter how small — makes this repo better for every future learner who finds it.

**Welcome to the contributor family. 🐍**

---

*This document is itself open to improvement. If anything here is unclear, open an issue!*
