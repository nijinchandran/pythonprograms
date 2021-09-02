import re

n= input("enter to valdate")
x='^[A-Z]'\w'*[A-Z]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")