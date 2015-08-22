
#Bird Language

VOWELS = "aeiouy"

def translate(phrase):
    res = ""
    i = 0
    while i< len(phrase) :
        if phrase[i] in VOWELS :
            res+=phrase[i]
            i+=2
        elif phrase[i].isalpha():
            res+=phrase[i]
            i+=1
        else :
             res+=phrase[i]
        i+=1
    phrase = res
    return phrase

print("GG");