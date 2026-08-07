word = input('Enter the word you desire: ')
censor_multiplier = int(input('Enter the censor multiplier number: '))
length = len(word)
squarelength = (length ** 2) + censor_multiplier
censorship_block = squarelength * '#'
print(word)
print(censorship_block)