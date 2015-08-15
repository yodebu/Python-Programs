#Three Words

def three_words(words):
    a = words.split()
    c = 0
    for w in a:
        if w.isdigit():
            c=0
        else:
            c+=1
        if c>=3:
            return True
    return False;
