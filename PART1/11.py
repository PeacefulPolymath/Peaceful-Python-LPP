num = int(input('Enter the 3 digit number: '))
#example 425
#hundred digit is h , tens digit is t, ones digit is o
h = num // 100
to = num % 100
t = to //10
o = to % 10
print(h + t + o)
