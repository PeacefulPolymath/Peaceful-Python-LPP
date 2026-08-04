#Challenege 26
num = int(input('ENter the number: '))
if num % 2 == 0:
    print('Even')
else:
    print('False')

#challenge 27
score = int(input('Enter your score: '))
if 0<=score<60:
    print('F')
elif 60<=score<=69:
    print('D')
elif 70<=score<=79:
    print('C')
elif 80<=score<=89:
    print('B')
elif 90<=score<=100:
    print('A')
else:
    print('Invalid Score')

#Challenge 28
year = int(input('Enter an year: '))
if (year % 4 == 0 and year % 100 != 0) or (year %4 == 0 and year %100 == 0 and year % 400 ==0):
    print('It is a Leap Year')
else:
    print('Not a Leap Year')

#Challenge 29
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
operator = input('ENter operator: ')
if operator == '+':
    result = num1+num2
elif operator == '-':
    result = num1 - num2
elif operator == '*' or operator == 'x':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print('Cannot divide with zero')
    else:
        result = num1 / num2
else:
    result = 'Invalid Operator'
print(result)