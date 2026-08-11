value = False
import random
def get_word_hint(secret_word , guess_word):
    if not len(guess_word) == 5:
        return 'Invalid Input!\n'
    hint = ''
    for i in range(5):
        if secret_word[i].lower() == guess_word[i].lower():
            hint += 'O'
        elif guess_word[i].lower() in secret_word.lower():
            hint += 'o'
        else:
            hint += 'x'
    return hint + '\n'

secret_word = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
secret_word = random.choice(secret_word)
print('Guess the secret five-letter word:')
for i in range(6):
    guess = input('')
    response = get_word_hint(secret_word , guess)
    print(response)
    if response.strip() == 'OOOOO':
        print('Your guess is correct')
        value = True
        break
if value == False:
    print(f'The secret word was {secret_word}. Better luck next time.')