#Flatten List

def flat_list(l):
    res = []
    for x in l :
        if not isinstance(x, list):
            res.append(x)
        else :
            res += flat_list(x)
    return res

print(flat_list([1, 2, 3]))
print(flat_list([1, [2, 2, 2], 4]))
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
print(flat_list([-1, [1, [-2], 1], -1]))
print(flat_list([[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]))
