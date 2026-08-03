# Python for Beginners - Part 3: Data Types and Operators

Welcome to Part 3! 🎉 Now that you know how to store things in variables and write basic statements, it's time to understand **what kind of things** you can store and **what you can do** with them. Think of it like learning about different materials (wood, metal, plastic) and the tools you can use on each.

We'll cover:
- The main **data types** in Python (text, numbers, true/false)
- How to check and **convert** types
- **Operators** – the symbols that let you work with your data

---

## 1. Data Types – What Kind of Information?

Python automatically figures out the type of data you put in a variable. Here are the most common ones you'll use:

| Type       | What it holds         | Example              |
|------------|-----------------------|----------------------|
| `str`      | Text (string)         | `"Hello"`, `'Roger'` |
| `int`      | Whole numbers         | `42`, `-3`, `0`      |
| `float`    | Decimal numbers       | `3.14`, `-0.5`, `2.0`|
| `bool`     | True or False         | `True`, `False`      |

Let's see them in action:

```python
name = "Roger"          # str
age = 8                 # int
height = 1.75           # float
is_dog = True           # bool

print(name)   # Roger
print(age)    # 8
print(height) # 1.75
print(is_dog) # True
```

**Important:** Python knows the type automatically. You don't need to declare it like in other languages.

### How to Check the Type

Use the built-in `type()` function:

```python
name = "Roger"
print(type(name))   # <class 'str'>

age = 8
print(type(age))    # <class 'int'>

height = 1.75
print(type(height)) # <class 'float'>

is_dog = True
print(type(is_dog)) # <class 'bool'>
```

You can also check if a variable is a specific type using `isinstance()`:

```python
name = "Roger"
print(isinstance(name, str))   # True
print(isinstance(name, int))   # False
```

---

## 2. Type Conversion – Changing Types

Sometimes you have a number that you want to treat as text, or vice versa. Python lets you convert between types using the type names as functions:

- `int()` – convert to whole number
- `float()` – convert to decimal
- `str()` – convert to text

### Examples:

**Convert string to number:**
```python
age_text = "8"
age_number = int(age_text)   # now it's an int
print(age_number + 2)        # 10
```

**Convert number to string:**
```python
age = 8
message = "I am " + str(age) + " years old"
print(message)   # I am 8 years old
```

**Convert float to int (truncates, doesn't round):**
```python
pi = 3.99
pi_int = int(pi)   # 3 (it cuts off the decimal)
```

**Convert int to float:**
```python
num = 5
num_float = float(num)   # 5.0
```

**Important:** Not everything can be converted. `int("hello")` would cause an error because "hello" isn't a number.

---

## 3. Operators – The Tools to Work with Data

Operators are special symbols that tell Python to perform operations on your data.

### 3.1 Assignment Operator `=`

You already know this one – it assigns a value to a variable:

```python
x = 10
name = "Alice"
```

### 3.2 Arithmetic Operators – Math!

| Operator | Meaning               | Example        | Result |
|----------|-----------------------|----------------|--------|
| `+`      | Addition              | `5 + 3`        | `8`    |
| `-`      | Subtraction           | `5 - 3`        | `2`    |
| `*`      | Multiplication        | `5 * 3`        | `15`   |
| `/`      | Division (float)      | `5 / 2`        | `2.5`  |
| `//`     | Floor division (int)  | `5 // 2`       | `2`    |
| `%`      | Modulo (remainder)    | `5 % 2`        | `1`    |
| `**`     | Exponentiation (power)| `5 ** 2`       | `25`   |

**Try these:**
```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
print(10 % 3)   # 1 (remainder)
print(10 ** 3)  # 1000
```

**String concatenation with `+`:** You can also use `+` to join strings:
```python
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World
```

### 3.3 Comparison Operators – Asking Questions

These compare two values and give you `True` or `False`.

| Operator | Meaning                 | Example      | Result |
|----------|-------------------------|--------------|--------|
| `==`     | Equal to                | `5 == 5`     | `True` |
| `!=`     | Not equal to            | `5 != 3`     | `True` |
| `>`      | Greater than            | `5 > 3`      | `True` |
| `<`      | Less than               | `5 < 3`      | `False`|
| `>=`     | Greater than or equal   | `5 >= 5`     | `True` |
| `<=`     | Less than or equal      | `5 <= 3`     | `False`|

```python
a = 10
b = 20
print(a == b)   # False
print(a < b)    # True
print(a != b)   # True
```

### 3.4 Logical Operators – Combining Conditions

| Operator | Meaning               | Example                          | Result |
|----------|-----------------------|----------------------------------|--------|
| `and`    | True if both true     | `(5 > 3) and (10 > 5)`           | `True` |
| `or`     | True if at least one  | `(5 > 3) or (10 < 5)`            | `True` |
| `not`    | Inverts truth value   | `not (5 > 3)`                    | `False`|

```python
age = 16
has_license = True

# Can this person drive? (age >= 18 AND has license)
can_drive = (age >= 18) and has_license
print(can_drive)   # False

# Can they enter a 16+ event?
can_enter = (age >= 16) or has_license
print(can_enter)   # True (they meet the age requirement)
```

**A common catch with `or` and `and` in Python:**

- `or` returns the first **truthy** value, or the last if all are falsy.
- `and` returns the first **falsy** value, or the last if all are truthy.

But for a beginner, just treat them as logical AND/OR that return `True`/`False` when used in conditions. You can safely ignore that nuance for now.

### 3.5 Special Operators: `in` and `is`

- `in` checks if something is inside a container (like a string or list). We'll use it more later.
- `is` checks if two variables refer to the exact same object. For basics, don't worry too much; use `==` for equality.

Example with `in`:
```python
name = "Roger"
print("R" in name)   # True
print("z" in name)   # False
```

---

## 4. Compound Assignment Operators – Shortcuts

These let you perform an operation and assign the result back to the same variable in one step.

| Operator | Equivalent to       |
|----------|---------------------|
| `+=`     | `x = x + y`         |
| `-=`     | `x = x - y`         |
| `*=`     | `x = x * y`         |
| `/=`     | `x = x / y`         |
| `%=`     | `x = x % y`         |
| `**=`    | `x = x ** y`        |

```python
score = 10
score += 5   # score becomes 15
score *= 2   # score becomes 30
print(score) # 30
```

---

## 5. The Ternary Operator – One-Line If/Else

You've seen `if` statements? The ternary operator is a shortcut for a simple `if-else` that returns a value.

**Syntax:**
```python
value_if_true if condition else value_if_false
```

**Example:**
```python
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)   # Minor
```

Without ternary, you'd write:
```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

Ternary is great for simple conditions, but don't overuse it – readability matters!

---

## Practice Challenges

### Challenge 8 – Type Detective
Write a program that:
- Creates variables for your name (string), your age (int), your height in meters (float), and whether you're a student (bool)
- Prints the type of each variable using `type()`

**Solution:**
```python
name = "Jamie"
age = 14
height = 1.65
is_student = True

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

### Challenge 9 – Temperature Converter
Write a program that:
- Stores a temperature in Celsius (as a float)
- Converts it to Fahrenheit using the formula: `F = C * 9/5 + 32`
- Prints both the Celsius and Fahrenheit values (as nice sentences)

**Solution:**
```python
celsius = 25.0
fahrenheit = celsius * 9/5 + 32

print(str(celsius) + "°C is " + str(fahrenheit) + "°F")
# Output: 25.0°C is 77.0°F
```

### Challenge 10 – Comparison Game
Given:
```python
a = 15
b = 10
c = 20
```
Write expressions using comparison and logical operators that evaluate to:
1. `True` if `a` is greater than `b` AND `c` is greater than `a`
2. `True` if `a` is less than `b` OR `c` is greater than `b`
3. `True` if `a` is NOT equal to `c`

**Solution:**
```python
a = 15
b = 10
c = 20

result1 = (a > b) and (c > a)   # True
result2 = (a < b) or (c > b)    # True (because c > b)
result3 = a != c                # True
```

### Challenge 11 – Ternary Fun
Write a program that:
- Stores a number in a variable
- Uses the ternary operator to determine if the number is even or odd (even means divisible by 2)
- Prints the result

**Solution:**
```python
num = 7
even_odd = "Even" if num % 2 == 0 else "Odd"
print(num, "is", even_odd)   # 7 is Odd
```

---

## Quick Quiz

1. **What data type would `3.14` be?**
   - `float`

2. **How do you convert the string "25" to an integer?**
   - `int("25")`

3. **What is `10 // 3`?**
   - `3` (floor division)

4. **What does `10 % 3` give?**
   - `1` (remainder)

5. **Which operator checks if two values are equal?**
   - `==`

6. **What does `(5 > 3) and (2 > 5)` return?**
   - `False` (because second part is false)

7. **What is the result of `not (5 == 5)`?**
   - `False` (not True = False)

8. **Write a ternary expression that returns "Pass" if score >= 60 else "Fail".**
   - `result = "Pass" if score >= 60 else "Fail"`

---

## Summary Checklist ✅

- [ ] I know the main data types: `str`, `int`, `float`, `bool`
- [ ] I can check type with `type()` and `isinstance()`
- [ ] I can convert between types using `int()`, `float()`, `str()`
- [ ] I can use arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- [ ] I can compare values with comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- [ ] I can combine conditions with logical operators (`and`, `or`, `not`)
- [ ] I understand compound assignment operators (`+=`, `-=`, etc.)
- [ ] I can write a simple ternary expression

---

## What's Next?

Next time we'll dive deeper into the specific types:
- **Strings** – all the cool things you can do with text (slicing, methods, formatting)
- **Booleans** – more about truthy/falsy values and using `any()`/`all()`
- **Numbers** – more math utilities and built-in functions

But you already have enough to start playing! Try to combine what you've learned to build small calculators or decision-makers.

See you in Part 4! 🐍