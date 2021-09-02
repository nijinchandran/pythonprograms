import re

n= input("enter the num to valdate")
x='[a-zA-Z]+\d$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")