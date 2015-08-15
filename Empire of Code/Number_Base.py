def convert(s, b):
    ans = 0;
    sy = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in s :
        if sy.index(c)>=b:
            return -1
        ans = ans*b + sy.index(c)
    return ans

print(convert("AF", 16))
print(convert("101", 2))
print(convert("101", 5))
print(convert("Z", 36))
print(convert("AB", 10))
