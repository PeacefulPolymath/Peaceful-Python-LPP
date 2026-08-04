#Challenge 12
messy = " PyThOn Is FuN! "
final = messy.strip().lower().replace('fun' , 'awesome')
print(final)

#challenge 13
ask = input('Enter your text ')
print('Length:' , ask)
the = ask.startswith('The')
if the:
    print(f'The word starts with The')
else:
    print('THe word does not start with The')
period = ask.endswith('.')
if period:
    print('There is a period at the end')
else:
    print('There is no period at the end')
capital = ask.upper()
print('The text in capitals is', capital)
titled = ask.title()
print('The text converted into a title is' , titled)

#Challenge 14
string = 'hello, world!'
hello = string[:4]
world = string[-6:-2]
reverse = string[-1:]
evened = string[0 : :2]

#challenge 15
scores = [85 , 72 , 93 , 60]
any(scores) > 90
all(scores) > 70

answers = [True , False , True]
not any(answers)

#Challeneg 16
name = 'Elena'
age = 15
city = 'Berlin'
hobby = 'painting'
print(f'{name} is {age} years old. She lives in {city} and loves {hobby}.')

#Challenge 17
from enum import Enum
class weekday(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

print(weekday.WED.value)
print(weekday.WED.name)
print(weekday.FRI.value)
print(weekday.FRI.name)