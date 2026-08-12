def spongecase(sentence):
    if not isinstance(sentence , str):
        return 'Invalid Input'
    new_sentence = ''
    convert = 'lower'
    for i in sentence:
        if i.isalpha():
            if convert == 'lower':
                new_sentence += i.lower()
                convert = 'upper'
            elif convert == 'upper':
                new_sentence += i.upper()
                convert = 'lower'
        else:
            new_sentence += i
    return new_sentence

sentence = input('Enter your sentence: \n')
print(spongecase(sentence))