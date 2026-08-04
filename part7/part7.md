I see you've already completed **Part 6** (Control Statements) – and you even included the solutions! Great job! 👏

Since you said **"next"**, let's move forward. The next big topic is **Lists** – one of the most useful data structures in Python. It's like a super‑powered container that can hold many items, and you can add, remove, or change them easily.

---

# Python for Beginners - Part 7: Lists (Your First Data Collection)

Welcome to **Part 7**! 🎉  
You've learned to make decisions with `if`/`else`. Now imagine you want to store a whole collection of things – like a shopping list, a list of your friends' names, or scores from a game. **Lists** are perfect for that.

We'll cover:
- What a **list** is and how to create one
- Accessing items by **index** (position)
- **Slicing** – grabbing a sub‑list
- **Changing, adding, and removing** items
- Useful **list methods** (`append`, `insert`, `remove`, `pop`, `sort`, etc.)
- Checking if something is **in** a list
- **Loops** over lists (a sneak peek)
- Copying lists (to avoid accidental changes)

---

## 1. What is a List?

A **list** is an ordered collection of items. You create it with square brackets `[]`, separating items with commas.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]   # lists can hold different types!
empty = []   # an empty list
```

Lists can hold **anything** – numbers, strings, even other lists!

---

## 2. Accessing Items by Index

Each item in a list has a **position** (index), starting from **0** for the first item.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # cherry
```

Negative indices count from the end:
```python
print(fruits[-1])   # cherry
print(fruits[-2])   # banana
```

You can change an item by assigning to its index:
```python
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']
```

---

## 3. Slicing – Getting a Sub‑list

Use the same slicing syntax as strings: `list[start:end]` (end is exclusive).

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[-2:])   # [40, 50]
```

You can also use a step:
```python
print(numbers[::2])   # [10, 30, 50]  (every second)
```

---

## 4. Useful List Methods

Lists come with many built‑in methods that let you manipulate them easily.

| Method                | What it does                         | Example                     |
|-----------------------|--------------------------------------|-----------------------------|
| `append(item)`        | Adds item to the end                 | `fruits.append("orange")`   |
| `insert(index, item)` | Inserts at a specific position       | `fruits.insert(1, "mango")` |
| `remove(item)`        | Removes the first occurrence         | `fruits.remove("banana")`   |
| `pop(index)`          | Removes and returns item at index (default last) | `fruits.pop()` |
| `index(item)`         | Returns the index of first occurrence| `fruits.index("apple")`     |
| `count(item)`         | Counts how many times item appears   | `fruits.count("apple")`     |
| `sort()`              | Sorts the list (in‑place)            | `numbers.sort()`            |
| `reverse()`           | Reverses the list (in‑place)         | `fruits.reverse()`          |
| `copy()`              | Returns a shallow copy of the list   | `new = fruits.copy()`       |

**Important:** `sort()` and `reverse()` change the original list. They don't return a new one.

```python
nums = [5, 2, 8, 1]
nums.sort()
print(nums)   # [1, 2, 5, 8]

nums.append(10)
print(nums)   # [1, 2, 5, 8, 10]
```

---

## 5. Checking If an Item is in the List

Use the `in` operator (returns `True` or `False`):

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("grape" in fruits)    # False
```

You can also use `not in`:
```python
if "grape" not in fruits:
    print("We need grapes!")
```

---

## 6. Looping Over Lists (Quick Intro)

You can go through each item in a list using a `for` loop (we'll cover loops in detail later, but this is useful now):

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

Output:
```
I like apple
I like banana
I like cherry
```

---

## 7. Copying Lists

If you do `new_list = my_list`, both variables point to the **same** list – changing one changes the other. To create an independent copy, use:

```python
original = [1, 2, 3]
copy1 = original.copy()          # method
copy2 = original[:]              # slicing
```

Now changes to `copy1` won't affect `original`.

---

## 8. List Length and Other Built‑ins

- `len(list)` – number of items
- `min(list)` – smallest value (if comparable)
- `max(list)` – largest value
- `sum(list)` – sum of numbers
- `sorted(list)` – returns a new sorted list (doesn't change original)

---

## Practice Challenges 🏆

**Challenge 30 – Shopping List Manager**
Create an empty list called `shopping_list`. Write a program that repeatedly asks the user:
- "Add an item (or 'done' to finish): "
- Add each item to the list.
- After the user types 'done', print the final shopping list.

*Hint: use a `while` loop with a condition, but you can also just use `for` if you decide the number of items upfront. For this, use `while True` with `break` when 'done' is entered.*

---

**Challenge 31 – List Statistics**
Ask the user to enter 5 numbers (use a loop). Store them in a list. Then print:
- The list
- The sum of all numbers
- The average (sum / length)
- The largest number
- The smallest number

*(Do not use `sum()`, `min()`, `max()` – implement your own logic with loops.)*

---

**Challenge 32 – Remove Duplicates**
Given a list `items = [1, 2, 2, 3, 4, 4, 5]`, write a program that creates a new list with only the unique items (remove duplicates). Print the new list.

*Hint: you can check if an item is already in the new list before adding it.*

---

**Challenge 33 – Reverse a List (Without Using reverse() or slicing)**
Ask the user for a list of numbers (you can decide how many). Then print the list in reverse order **without** using `reverse()` or `[::-1]`. Use a loop to swap elements or build a new list.

---

**Challenge 34 – Find the Index**
Ask the user for a list of names (enter them one by one, stop with 'done'). Then ask for a name to search for. If the name is in the list, print its index (position). If not, print "Not found".  
*(You can use the `index()` method, but try to implement it manually with a loop for practice.)*

---

**Challenge 35 – To‑Do List (Add and Remove)**
Create an empty list `tasks`. Write a program that shows a menu:
1. Add a task
2. Remove a task (by name)
3. Show all tasks
4. Exit
Keep asking until the user chooses exit. Use a `while` loop and `if/elif` to handle choices.

---

## Quick Quiz (No solutions – try yourself!)

1. How do you create an empty list?
2. What is the index of the first element in a list?
3. How do you add an item to the end of a list?
4. How do you insert an item at a specific position?
5. What does `list.pop()` do?
6. How do you check if an item is in a list?
7. How do you get the number of items in a list?
8. Why is `new = old` not a copy? How do you make a proper copy?

---

## Summary Checklist ✅

- [ ] I can create a list with square brackets
- [ ] I can access and change items by index
- [ ] I can slice a list to get a sub‑list
- [ ] I can use `append()`, `insert()`, `remove()`, `pop()`
- [ ] I can sort and reverse a list
- [ ] I can check membership with `in`
- [ ] I can loop over a list with `for`
- [ ] I understand the difference between copying and referencing

---

## What's Next?

In **Part 8**, we'll explore **Tuples** – lists' immutable cousins – and **Dictionaries** – which let you store data as key‑value pairs (like a real‑life dictionary). You'll be able to organize data in powerful ways.

Keep practicing with the challenges – don't peek at solutions until you've tried them yourself! 🐍

See you in Part 8!