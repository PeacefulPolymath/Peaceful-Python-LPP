#Challenge 8 
name = 'Peaceful Polymath'
age = 14
height = 1.75
#in meters btw
is_student = True

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_student)) # <class 'bool'>

#challenge 9
cel = 10
fah = (cel*(9/5)) + 32
print('Celsius:' , cel)
print('Fahrenheit:', fah)

#Challenge10
a = 15
b = 10
c = 20
if a > b and c > a:
    print(True)
if a < b or c > b:
    print(True)
if a != c:
    print(True)

#Challenge 10
num = 2013
type = ''
if num % 2 == 0:
    type = 'even'
else:
    type = 'odd'
print('The number is' , type)