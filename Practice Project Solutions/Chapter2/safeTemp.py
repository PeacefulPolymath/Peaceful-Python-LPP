#Code with bugs
'''
print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if scale == 'C':
    if degrees >= 16 or degrees <= 38:
        print('Dangerous')
    else:
        print('Dangerous')
elif scale == 'F':
    if degrees > 60.8 and degrees >= 100.4:
        print('Safe')
    else:
        print('Dangerous')
'''

#Fixed Code
print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if scale == 'C':
    if 16 <= degrees <= 38:
        print('Safe')
    else:
        print('Dangerous')
elif scale == 'F':
    if 60.8 <= degrees <= 100.4 :
        print('Safe')
    else:
        print('Dangerous')