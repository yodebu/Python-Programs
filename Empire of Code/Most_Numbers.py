#Most Numbers

def most_difference(*args):
    if len(args)==0:
        return 0
    return max(args) - min(args)
