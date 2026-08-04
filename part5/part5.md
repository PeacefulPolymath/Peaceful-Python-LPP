# Python for Beginners - Part 5: Numbers (Deep Dive) and User Input

Welcome back! 🎉 You already know how to store numbers and do basic math. But numbers in Python are more powerful than you might think. In this lesson, we'll explore all the cool things you can do with numbers, including special modules for precise calculations, and we'll also learn how to get **input from the user** – making your programs interactive!

We'll cover:
- **Integers, Floats, and Complex** – a quick refresher
- **Built‑in functions** for numbers (`abs()`, `round()`, `pow()`, etc.)
- The **`math`** module – your Swiss Army knife for math
- **`decimal`** and **`fractions`** – for when you need perfect precision
- **Constants** and **Enums** – a quick recap
- **User Input** – making your program talk to the user
- Lots of practice challenges

Let's dive in!

---

## 1. Numbers – A Quick Refresher

Python has three main numeric types:

| Type      | What it is                    | Example           |
|-----------|-------------------------------|-------------------|
| `int`     | Whole numbers (positive, zero, negative) | `42`, `-3`, `0`   |
| `float`   | Decimal numbers               | `3.14`, `-0.5`, `2.0` |
| `complex` | Numbers with real and imaginary parts | `2+3j`, `1-2j`    |

You create them simply by writing the number:

```python
age = 8          # int
pi = 3.14159     # float
z = 2 + 3j       # complex
```

You can check the type with `type()`.

---

## 2. Built‑in Functions for Numbers

Python gives you some handy functions right out of the box – no imports needed!

### `abs()` – Absolute Value

Returns the distance from zero, always positive:

```python
print(abs(-5))     # 5
print(abs(3.7))    # 3.7
```

### `round()` – Round a Number

Rounds to the nearest integer by default. You can also specify how many decimal places:

```python
print(round(3.14159))      # 3
print(round(3.14159, 2))   # 3.14
print(round(2.5))          # 2 (Python uses "banker's rounding" – ties go to even)
```

### `pow()` – Power (Exponentiation)

Computes `x` raised to the power `y`. You can also use `**`:

```python
print(pow(2, 3))   # 8
print(2 ** 3)      # same
```

### `min()` and `max()` – Find the Smallest/Largest

```python
print(min(5, 2, 9, 1))   # 1
print(max(5, 2, 9, 1))   # 9
```

### `sum()` – Add All Numbers in a List

```python
numbers = [1, 2, 3, 4]
print(sum(numbers))   # 10
```

---

## 3. The `math` Module – Advanced Math

For more advanced math (square roots, trigonometry, logarithms, constants like π), we use the `math` module. You need to import it first:

```python
import math
```

Now you have access to many functions:

- `math.sqrt(x)` – square root
- `math.sin(x)`, `math.cos(x)`, `math.tan(x)` – trigonometry (angles in radians)
- `math.log(x)` – natural logarithm
- `math.log10(x)` – base‑10 logarithm
- `math.ceil(x)` – round up
- `math.floor(x)` – round down
- `math.factorial(x)` – factorial (e.g., 5! = 120)
- `math.pi` – π ≈ 3.14159
- `math.e` – Euler's number ≈ 2.71828

**Example:**

```python
import math

print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.141592653589793
print(math.factorial(5))    # 120
print(math.ceil(3.2))       # 4
print(math.floor(3.8))      # 3
```

You can also import specific functions:

```python
from math import sqrt, pi
print(sqrt(25))   # 5.0
print(pi)         # 3.1415...
```

---

## 4. Precision Matters – `decimal` and `fractions`

Floating‑point numbers (like `0.1`) are stored in binary, and sometimes they're not exactly what you think:

```python
print(0.1 + 0.2)   # 0.30000000000000004  😲
```

This is because of how computers represent decimals. For financial or scientific calculations where you need exact decimal math, use the `decimal` module.

### `decimal.Decimal`

```python
from decimal import Decimal

price = Decimal('0.10')
total = price * 3
print(total)   # 0.30 (exact!)
```

You can also set precision (how many decimal places) globally.

### `fractions.Fraction` – Rational Numbers

For exact fractions (like 1/3), use the `fractions` module:

```python
from fractions import Fraction

f = Fraction(1, 3)   # 1/3
print(f * 3)         # 1 (exactly)
```

These modules are powerful when you need perfect accuracy.

---

## 5. Constants and Enums – Quick Recap

### Constants (by convention)

In Python, we **cannot** enforce a constant, but we use **ALL_CAPS** names to tell other programmers "don't change this":

```python
MAX_SPEED = 120
PI = 3.14159
```

### Enums

Enums give meaningful names to sets of constant values. You already saw them:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Usage
print(Color.RED)        # Color.RED
print(Color.RED.value)  # 1
```

They make your code more readable and less error‑prone.

---

## 6. User Input – Talking to Your Program

Now for the fun part! You can make your program **ask** the user for information using `input()`.

### How it works

- `input()` displays a prompt (optional) and waits for the user to type something and press Enter.
- It **always returns a string** – even if the user types a number!

**Simple example:**

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

### Converting Input

Since `input()` returns a string, you need to convert it if you want a number:

```python
age_string = input("How old are you? ")
age = int(age_string)   # now it's an integer
print("Next year you'll be", age + 1)
```

You can also convert to `float`:

```python
height = float(input("Enter your height in meters: "))
```

### Handling Bad Input (a sneak peek)

What if the user types "abc" when you asked for a number? The program crashes with a `ValueError`. Later we'll learn about `try`/`except` to handle this gracefully, but for now, just be aware that you should trust the user... or not! 😄

### Multiple Inputs

You can ask for several pieces of information:

```python
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

print(f"{name} is {age} years old and lives in {city}.")
```

---

## 7. Putting It All Together – A Simple Interactive Program

Here's a mini‑project that combines numbers, math, and user input:

```python
import math

print("=== Circle Area Calculator ===")
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")          # :.2f rounds to 2 decimals
print(f"Circumference: {circumference:.2f}")
```

---

## Practice Challenges 🏆

### Challenge 18 – Absolute Difference
Ask the user for two numbers. Calculate and print the absolute difference between them (the positive distance). Use `abs()`.

### Challenge 19 – Pythagorean Theorem
Write a program that asks for the lengths of the two shorter sides of a right‑triangle (a and b). Calculate and print the hypotenuse (c) using `math.sqrt(a**2 + b**2)`.

### Challenge 20 – Precision Shopping
Ask the user for the price of an item (as a decimal) and the quantity. Use the `Decimal` module to calculate the total cost exactly. Print it.

### Challenge 21 – Factorial Fun
Ask the user for a non‑negative integer. Print its factorial using `math.factorial()`.

### Challenge 22 – Temperature Converter with User Input
Ask the user to enter a temperature in Celsius. Convert it to Fahrenheit using the formula `F = C * 9/5 + 32`. Print the result nicely with one decimal place.

### Challenge 23 – Enum and User Choice
Define an enum `Day` with the seven days of the week (assign values 1–7). Ask the user for a number (1–7) and print the name of the corresponding day. (Hint: you can use `Day(number)` to get the enum member.)

### Challenge 24 – Circle Calculator
Write a program that asks the user for the radius of a circle. Calculate and print:
- The diameter (2 * radius)
- The area (π * r²)
- The circumference (2 * π * r)
Use `math.pi` and format the output to two decimal places.

### Challenge 25 – Guess the Number (mini game – no solution)
Write a program that:
- Stores a secret number (e.g., `secret = 7`)
- Asks the user to guess the number
- If the guess is correct, print "You got it!"
- If the guess is too high, print "Too high!"; if too low, print "Too low!"
- **Hint:** You'll need `if` statements – we'll cover them properly in the next lesson, but try to figure it out!

---

## Quick Quiz (Test Yourself!)

1. What does `abs(-7.5)` return?
2. How do you round `3.14159` to 2 decimal places?
3. Which module would you import to get `sqrt()` and `pi`?
4. What is the difference between `float` and `Decimal`?
5. What does `input()` always return – a string or a number?
6. How do you convert the result of `input()` to an integer?
7. Write a one‑line expression that uses `pow()` to calculate 2 to the power of 10.
8. What is the convention for naming a constant in Python?

---

## Summary Checklist ✅

- [ ] I understand `int`, `float`, and `complex` numbers
- [ ] I can use `abs()`, `round()`, `pow()`, `min()`, `max()`, `sum()`
- [ ] I can import and use the `math` module
- [ ] I know about `decimal` and `fractions` for precision
- [ ] I remember constants (ALL_CAPS) and enums
- [ ] I can use `input()` to get user input
- [ ] I can convert input to numbers using `int()` or `float()`

---

## What's Next?

In **Part 6**, we'll finally get into **Control Statements** – `if`, `elif`, `else` – which let your program make decisions. Combine that with user input, and you can build games, quizzes, and interactive tools!

See you there! 🐍