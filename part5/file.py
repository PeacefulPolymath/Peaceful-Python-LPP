#CHallenge 18
num1 = int(input('Enter your desired number 1: '))
num2 = int(input('Enter your desired number 2: '))
dif = num2 - num1
finaldif = abs(dif)
print('Theabsolute difference between the given numbers is' , finaldif)

#challenge 19
from math import sqrt
base = int(input('ENter the length of the base in a right angle triangle: '))
perp = int(input('Enter the length of the perpendicular in a right angle triangle: '))
hyp = sqrt(base**2 + perp**2)
print('Then, Hypotenuse is' , hyp)

#Challenge 20
from decimal import Decimal
price = Decimal(input('Enter the price: '))
quantity = int(input('ENter the quantity: '))
cost = price * quantity
print('The total cost is' , cost)


#Challenge 21
from math import factorial
ask = int(input('Enter a non negative integral number: '))
if ask < 0:
    print('Wrong input')
else:
    print(factorial(ask))


#Challenge 22
#Already done Try it yourself

#Challenge 23
from enum import Enum
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6 
    SUNDAY = 7
day = int(input('Enter a number between 1 and 7:'))
if day > 7:
    print('Invalid input')
else:
    print(Day(day).name)

#Challenge 24
from math import pi
radius = int(input('Enter radius: '))
area = round(pi * (radius**2) , 2)
circum = round(2 * pi * radius , 2)
print(area)
print(circum)

#Challenge 25
secret = 9
user = int(input('Guess the number: '))
if secret == user:
    print('Your guess is correct')
elif secret > user:
    print('Your guess is lower than the secret number')
else:
    print('Your guess is greater than the secret number')
