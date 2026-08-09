size = int(input('Enter the tree size (Numbers only): \n'))
space = size - 1
chars = 1
for i in range(size):
    print(space*' ' + chars *'^' + space*' ' )
    space -= 1
    chars += 2
trunk = (size-1)*' '+ '#\n' + (size-1)*' '+ '#\n'
print(trunk)
