You got it! 👍

**Part 8 starts with exercise number 36** – and I'll keep the quality high, not just filler.

Here are **6 solid, meaningful challenges** that actually test your understanding of tuples and dictionaries – no busywork!

---

# Part 8 – Tuples and Dictionaries (Quality Challenges)

---

## Challenge 36 – Coordinate Distance Calculator
Create a tuple for point A (x1, y1) and another tuple for point B (x2, y2). Write a program that calculates the **Euclidean distance** between them using the formula:

\[
\text{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

*Hint: import `math` and use `math.sqrt()`.*

---

## Challenge 37 – Phonebook Manager (Dictionary)
Create an empty dictionary called `phonebook`. Write a menu‑driven program that allows the user to:
1. **Add** a contact (name and phone number)
2. **Look up** a contact by name (print number or "Not found")
3. **Delete** a contact by name
4. **Show all** contacts (formatted nicely)
5. **Exit**

Use a `while` loop and `if/elif` – no half‑baked solutions. Make it user‑friendly.

---

## Challenge 38 – Word Frequency Counter (Dictionary)
Ask the user to enter a sentence. Use `split()` to break it into words. Count how many times **each** word appears. Print the results sorted alphabetically.

*Example input:* `"apple banana apple cherry banana apple"`  
*Output:*
```
apple: 3
banana: 2
cherry: 1
```

**Bonus:** Remove punctuation (`.`, `,`, `!`, `?`) before counting.

---

## Challenge 39 – Student Gradebook (Nested Dictionary)
Create a dictionary called `students` where:
- Each key is a student name (string)
- Each value is **another dictionary** with keys: `"age"`, `"grade"`, and `"subjects"` (a list of subjects)

Add at least **4 students** with different data.

Then write code that:
1. Prints the name and grade of every student.
2. Prints the subjects of a specific student (ask the user for the name).
3. Calculates and prints the **average grade** of all students.

---

## Challenge 40 – Tuple Unpacking and Min/Max
Ask the user to enter a list of numbers (separated by spaces). Use `split()` and convert to integers. Store them in a list. Then:
- Create a tuple from that list.
- Write a function that returns **two values**: the minimum and maximum numbers (as a tuple).
- Unpack the returned tuple and print: `"Min: X, Max: Y"`.

*Do **not** use `min()` or `max()` – implement your own logic with a loop.*

---

## Challenge 41 – Inventory System (Dictionary of Dictionaries)
Create an inventory dictionary where:
- Each key is a product name (string)
- Each value is a dictionary with keys: `"price"` (float) and `"stock"` (int)

Add at least 5 products.

Write a program that:
1. Prints all products with their price and stock.
2. Asks the user for a product name and prints its details.
3. Asks the user for a product name and a quantity to purchase. If stock is sufficient, reduce stock and print a confirmation. If not, print "Insufficient stock".

---

## Challenge 42 – Merge Two Dictionaries
Write a program that:
- Creates two dictionaries with some overlapping keys.
- Merges them into a third dictionary.
- If a key exists in both, the value from the second dictionary should overwrite the first.

*Example:*
```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5}
# Result: {"a": 1, "b": 4, "c": 3, "d": 5}
```

Do **not** use built‑in `update()` – implement it with a loop.

---

## Quick Quiz (No solutions – figure them out!)

1. What's the difference between a list and a tuple?
2. Can a tuple be used as a dictionary key? Why or why not?
3. What does `dict.get(key, default)` do?
4. How do you loop over both keys and values in a dictionary?
5. How do you check if a key exists in a dictionary?
6. What happens if you try to add a key that already exists in a dictionary?
7. Why would you choose a dictionary over a list for storing user information?
8. Can a dictionary have a list as a key? Why or why not?

---

## Summary Checklist ✅

- [ ] I can create and use tuples
- [ ] I understand tuple immutability and when to use tuples
- [ ] I can create dictionaries with key‑value pairs
- [ ] I can access, add, modify, and delete dictionary entries
- [ ] I can use `get()` to safely access values
- [ ] I can loop over dictionaries with `items()`
- [ ] I can create and work with nested dictionaries
- [ ] I understand the use cases for lists, tuples, and dictionaries

---

## What's Next?

**Part 9 – Loops** – this is where we finally dive deep into `for` and `while` loops. You'll learn to iterate efficiently, build powerful automation, and combine loops with lists, tuples, and dictionaries.

No filler – just solid, practical skills. 🐍

Ready when you are – just say **"next"** !