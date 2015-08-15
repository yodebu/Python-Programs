#Letter Queue

def letter_queue(com):
    a =[]
    for x in com:
        if x[1]=='U':
            a.append(x[5])
        elif len(a):
            a.pop(0)
    return "".join(a)
