def get_end_coordinate(directions):
    coordinates = [0 , 0]
    for i in directions:
        if i=='n':
            coordinates[1]+= 1
        elif i== 's':
            coordinates[1]-= 1
        elif i== 'e':
            coordinates[0] += 1
        elif i == 'w':
            coordinates[0] -= 1
        else:
            return 'Invalid Input'
    return coordinates
list = []
while True:
    enter = input('Enter N OR S OR W OR E for moving those respective directions: ').lower().strip()
    if enter in ['n' , 's' , 'e' , 'w']:
        list.append(enter)
    elif enter == '':
        break
print(get_end_coordinate(list))



