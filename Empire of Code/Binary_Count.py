#Binary Count

def count_units(n):
    return bin(n).count("1")

print(count_units(500))