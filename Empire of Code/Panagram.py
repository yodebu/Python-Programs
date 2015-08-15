#Pangram

def check_pangram(text):
    return set('QWERTYUIOPASDFGHJKLZXCVBNM') <= set(text.upper())


print(check_pangram("The quick brown fox jumps over the lazy dog."))
print(check_pangram("ABCDEF"))
print(check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"))
