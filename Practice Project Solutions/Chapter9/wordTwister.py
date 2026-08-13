import re
pattern = re.compile(r'\b(\w)(\w*)\b')
new = pattern.sub(r'\2\1' , 'Hello world! How are you? I am fine.')
print(new)