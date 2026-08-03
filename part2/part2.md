Python for Beginners - Part 2: Python Basics

Welcome back! 🎉 You've installed Python and run your first program. Now it's time to understand the building blocks of Python code. Think of this like learning the alphabet before you write sentences.

We'll cover:

    Variables (storing information)

    Expressions and statements (giving instructions)

    Comments (talking to humans)

    Indentation (the secret to Python's structure)

Let's dive in!
1. Variables - Your Information Boxes

In Python, a variable is like a labeled box where you can store things. You put something in, give it a name, and you can use it later.
How to Create a Variable

You use the = sign to assign (store) a value:
python

name = "Roger"          # storing text (called a string)
age = 8                 # storing a whole number
height = 1.75           # storing a decimal number
is_student = True       # storing True/False (boolean)

Think of it like:

    "Hey Python, remember that name means 'Roger' from now on!"

Rules for Variable Names

    Can contain letters, numbers, and underscores (_)

    Cannot start with a number

    Cannot be a Python keyword (like if, while, import)

✅ Valid:
python

my_name
age1
user_123
_name

❌ Invalid:
python

123age      # starts with a number
my-name     # contains a hyphen
if          # Python keyword

Using Variables

Once you've stored something, you can use it:
python

name = "Roger"
print(name)          # prints: Roger
print(name + " is cool!")  # prints: Roger is cool!

You can also change what's in the box:
python

age = 8
age = 9              # now age is 9
print(age)           # 9

Coding Challenge 💪

Challenge 4:
Create variables to store:

    Your first name

    Your last name

    Your age

    Your favorite color

Then print a sentence like:
"My name is Jamie Smith. I am 14 years old and I love blue!"

Solution:
python

first_name = "Jamie"
last_name = "Smith"
age = 14
favorite_color = "blue"

print("My name is " + first_name + " " + last_name + ". I am " + str(age) + " years old and I love " + favorite_color + "!")

    Note: We used str(age) because we can only add text to text. We'll learn more about that soon!

2. Expressions and Statements
Expressions - Things That Have a Value

An expression is anything that Python can calculate to give a value.

Examples:
python

5 + 3               # gives 8
"Hello" + "World"   # gives "HelloWorld"
age + 10            # if age is 8, gives 18
3 * 4               # gives 12

Every expression gives a result. You can use it directly.
Statements - Instructions That Do Something

A statement is a command that tells Python to do something.

Examples:
python

name = "Roger"      # assignment statement
print(name)         # function call statement
age = age + 1       # assignment with calculation

A program is a series of statements, one per line.

You can put multiple statements on one line using a semicolon (;), but it's not recommended (makes code messy):
python

name = "Roger"; print(name)   # works but not nice

Better to write:
python

name = "Roger"
print(name)

Quick Check

Question: Which of these is an expression?

    □

    print("Hi") (this is a statement)
    □

    2 + 2 (this is an expression) ✅
    □

    name = "Alex" (this is a statement)

3. Comments - Talking to Humans (and Future You!)

Comments are notes in your code that Python ignores. They're for people (like you and others) to understand what the code does.
How to Write Comments

Use # – everything after it on that line is ignored:
python

# This is a comment
name = "Roger"  # This is an inline comment

# The following line prints the name
print(name)

Why are comments useful?

    Remind yourself what your code does when you come back later

    Help other programmers understand your thinking

    Explain tricky parts

Bad comment (obvious):
python

x = 5   # set x to 5   (useless - we can see that!)

Good comment (explains why):
python

# We use 5 because the game board needs 5 players
max_players = 5

4. Indentation - Python's Superpower

In many languages, you use curly braces {} to group code. But Python uses indentation (spaces or tabs) – and it's mandatory!
What is Indentation?

It's the spaces at the beginning of a line. In Python, indentation tells Python which statements belong together.
Example: Wrong Way
python

name = "Flavio"
    print(name)    # This will cause an ERROR!

Why? Because print(name) is indented, but there's no reason for it. Python is confused.
When Do You Use Indentation?

We use indentation when we have blocks of code, like in:

    if statements (we'll learn soon)

    for and while loops

    Function definitions

    Class definitions

Example (correct):
python

age = 18

if age >= 18:
    print("You are an adult")    # indented 4 spaces
    print("You can vote")        # also indented
    # this whole block belongs to the if
print("This is outside the if")  # not indented

Rule: Use 4 spaces for each level of indentation. Most code editors will do this for you when you press Tab.
Challenge: Spot the Error

Challenge 5:
Which of these will cause an error?
python

# Code A
x = 10
if x > 5:
    print("Big")
    print("Number")

# Code B
y = 3
    print(y)

# Code C
if y < 5:
print("Small")

Solution:

    Code B has indentation with no reason → Error

    Code C has missing indentation inside the if → Error

    Code A is correct! ✅

5. Putting It All Together

Let's combine variables, expressions, statements, comments, and indentation in a mini-program:
python

# This program calculates the total price with tax
price = 100
tax_rate = 0.07   # 7% tax

# Calculate tax and total
tax = price * tax_rate
total = price + tax

# Show the result
print("Price: $", price)
print("Tax: $", tax)
print("Total: $", total)

Output:
text

Price: $ 100
Tax: $ 7.0
Total: $ 107.0

Practice Challenges
Challenge 6 - Simple Calculator

Write a program that:

    Stores two numbers in variables

    Adds them and prints the result

    Multiplies them and prints the result

Solution:
python

num1 = 12
num2 = 5

sum_result = num1 + num2
product_result = num1 * num2

print("Sum:", sum_result)
print("Product:", product_result)

Challenge 7 - Greeting Generator

Create variables for:

    Your name

    Your city

    Your favorite food

Print a paragraph introducing yourself using these variables.

Solution (example):
python

name = "Alex"
city = "London"
food = "pizza"

print("Hello! I'm " + name + ".")
print("I live in " + city + ".")
print("My favorite food is " + food + ".")

Summary Checklist ✅

    □

    I can create variables and assign values
    □

    I know the rules for naming variables
    □

    I understand the difference between expressions and statements
    □

    I know how to write comments
    □

    I understand why indentation matters and how to use it

What's Next?

In the next lesson, we'll explore Data Types:

    Strings (text)

    Numbers (integers and floats)

    Booleans (True/False)

    How to check what type something is

    Converting between types

We'll also start using operators (like +, -, *, /) more formally.
Quick Quiz

    What symbol is used to assign a value to a variable?
    → = (equals sign)

    Can a variable name start with a number?
    → No

    What does # do?
    → Starts a comment

    What happens if you forget to indent inside an if statement?
    → Python gives an IndentationError

    Which is an expression: 5 + 5 or x = 5 + 5?
    → 5 + 5 is an expression (it returns a value). The whole x = 5 + 5 is a statement.

Great work! You now understand the core syntax of Python. Next time, we'll dig into data types and operators. See you soon! 🐍
