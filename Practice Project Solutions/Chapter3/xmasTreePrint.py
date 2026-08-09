import random
size = int(input('Enter the tree size (Numbers only): \n'))
space = size - 1
chars = 1
text = ''
options = ['^' , '^' , 'o' , '^']
trunk = (size-1)*' '+ '#\n' + (size-1)*' '+ '#\n'
while True:
    if chars >= size*2:
        break
    else:
        text = ''
        for i in range(chars):
            text += random.choice(options)
        print(space*' ' + text + space*' ')
        space -= 1
        chars += 2
print(trunk)
        
