def printval(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(printval(3,4,6,7,8,9,0))