#Fizz Buzz

def fizz_buzz(n):
    if n%15==0:
        return "Fizz Buzz"
    if n%5==0:
        return "Buzz"
    if n%3==0:
        return "Fizz"
    return str(n)
