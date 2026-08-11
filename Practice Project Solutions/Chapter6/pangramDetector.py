def is_pangram(sentence):
    alphas = list("abcdefghijklmnopqrstuvwxyz")
    occurs = []
    sentence = sentence.lower()
    for i in sentence:
        if i in alphas:
            if i not in occurs:
                occurs.append(i)
    if len(occurs) == 26:
        return 'This sentence is a pangram'
    else:
        return 'This sentence is not a pangram'
#print(is_pangram('Hello, world!'))
        
