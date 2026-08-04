Great work! 🎉 You've successfully completed all the challenges for **Part 5 – Numbers and User Input**. Your code is now clean, correct, and runs without errors.

Now it's time to move on to the next big topic: **Control Statements** – `if`, `elif`, `else`. This is where your programs start to make decisions, respond to user input, and become truly interactive.

---

## Part 6 – Control Statements (if, elif, else)

In this lesson, you'll learn:

- How to write **conditional logic** – executing code only when certain conditions are met.
- The syntax of `if`, `elif`, and `else`.
- How to combine conditions with logical operators (`and`, `or`, `not`).
- How to use **comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`).
- How to nest conditions and handle multiple cases.

You'll be able to build:
- **Quizzes** that check answers.
- **Games** like "Guess the Number".
- **Interactive tools** that respond differently based on user input.
- **Validators** that ensure data is correct before using it.

---

## Quality Practice Challenges – Part 6

Here are **four focused challenges** that will help you master `if/elif/else`. Try them on your own – solutions are at the end of this message.

---

### 🔹 Challenge 26 – Even or Odd
Write a program that asks the user for an integer and prints:
- `"Even"` if the number is divisible by 2.
- `"Odd"` otherwise.

*Hint: Use the modulo operator `%` – a number is even if `number % 2 == 0`.*

---

### 🔹 Challenge 27 – Grade Calculator
Ask the user for a score (0–100). Print the corresponding letter grade:
- `A` for 90–100
- `B` for 80–89
- `C` for 70–79
- `D` for 60–69
- `F` for below 60

If the score is outside 0–100, print `"Invalid score"`.

---

### 🔹 Challenge 28 – Leap Year Checker
Ask the user for a year and determine if it's a leap year. A year is a leap year if:
- It is divisible by 4 **and**
- It is **not** divisible by 100, **unless** it is also divisible by 400.

Examples:
- 2020 → leap year
- 1900 → not leap year (divisible by 100 but not 400)
- 2000 → leap year (divisible by 400)

Print `"Leap year"` or `"Not a leap year"`.

---

### 🔹 Challenge 29 – Mini Calculator
Ask the user for two numbers and an operator (`+`, `-`, `*`, `/`). Perform the operation and print the result. If the operator is invalid, print `"Invalid operator"`.  
*Bonus: handle division by zero with an `if` check.*

---

That's it – only **four** exercises, each testing a different aspect of conditionals.

---

## Solutions (don't peek until you've tried!)

---

### Challenge 26 – Even or Odd
```python
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### Challenge 27 – Grade Calculator
```python
score = int(input("Enter score (0-100): "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

---

### Challenge 28 – Leap Year Checker
```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

---

### Challenge 29 – Mini Calculator
```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        result = "Error: division by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operator"

print(result)
```

---

## What’s next?

In **Part 7**, we'll dive into **loops** (`for` and `while`) – enabling your programs to repeat tasks efficiently. You'll combine loops with conditionals to build even more powerful applications.

Keep coding – you're building a solid foundation! 🐍