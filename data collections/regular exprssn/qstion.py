import re

n= input("enter to valdate")
x='[a-zA-Z]{8,15}\D^&$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
