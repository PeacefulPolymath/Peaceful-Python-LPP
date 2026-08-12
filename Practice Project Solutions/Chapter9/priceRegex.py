import re
def get_price(sentence):
    pattern = re.compile(r'\$\d+\.\d+')
    finds = pattern.findall(sentence)
    return finds
text = input('Enter the text: \n')
print(get_price(text))