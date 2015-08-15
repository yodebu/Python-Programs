#Triangle Angles

import math

def angles(a, b, c):
    a,b,c = sorted([a,b,c])
    if c > b+a:
        return [0]*3
    else:
        return [round(x) for x in sorted([ math.degrees(math.acos( (a*a + b*b - c*c)/(2*a*b)) ),
                              math.degrees(math.acos( (a*a - b*b + c*c)/(2*a*c)) ),
                              math.degrees(math.acos( (-a*a + b*b + c*c)/(2*b*c)) )])]

print(angles(4, 4, 4))
print(angles(3, 4, 5))
