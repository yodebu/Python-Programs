#Simple Areas

import math

def simple_areas(*args):
    
    if len(args)==1:
        return math.pi*args[0]*args[0]/4
    elif len(args)==2:
        return args[0]*args[1]
    else:
        a,b,c = args
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5
