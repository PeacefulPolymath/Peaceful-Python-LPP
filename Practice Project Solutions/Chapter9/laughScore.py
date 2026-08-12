import re
def laugh_score(laugh):
    pattern = re.compile(r'[hH][aA][hHaA]*')
    finds = pattern.search(laugh)
    score = 0
    if not finds:
        return 0
    else:
        matched_text = finds.group()
        return len(matched_text)
print(laugh_score('hahahahahahahahahahahhaaaaaaaahhaaaahhahhhaaaa'))