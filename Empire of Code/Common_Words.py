#Common Words

def common_words(a, b):
    return ",".join( sorted(set(a.split(',')) & set(b.split(','))) )



print(common_words("hello,world", "hello,earth"))
print(common_words("one,two,three", "four,five,six"))
print(common_words("one,two,three", "four,five,one,two,six,three"))
