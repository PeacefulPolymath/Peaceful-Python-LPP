import re
def get_hashtags(sentence):
    text = ''
    pattern = re.compile(r'#\S+')
    finds = pattern.findall(sentence)
    for i in finds:
        text += i + '\n'
    return text
text = input('Enter your sentence: \n')
print(get_hashtags(text))

