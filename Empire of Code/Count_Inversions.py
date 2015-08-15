#Count Inversion

def count_inversion(a):
    ans = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[j]<a[i]:
                ans+=1
    return ans


print(count_inversion((1, 2, 5, 3, 4, 7, 6)))
print(count_inversion((0, 1, 2, 3)))
print(count_inversion((99, -99)))
print(count_inversion((5, 3, 2, 1, 0)))
