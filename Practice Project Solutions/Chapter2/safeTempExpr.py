print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
condiiton1 = (scale == 'C' and (16 <= degrees <= 38))
condiiton2 = (scale == 'F' and (60.8 <= degrees <= 100.4))
if condiiton1 or condiiton2:
    print('Safe')
else:
    print('Dangerous')