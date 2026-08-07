minutes = int(input('Enter the number of minutes: '))
minperday = 60 * 24
minperhour = 60
days = minutes // minperday
minafterdays = minutes % minperday
hours = minafterdays // minperhour
minafterhours = minafterdays % minperhour

print(days , 'Days' , hours , 'Hours' , minafterhours , 'minutes')