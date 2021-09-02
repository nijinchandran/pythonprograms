import re
f1=open("phn num",'r')
x='[+][9][1]\d{10}$'
for num in f1:
    print(num)
    number=num.rstrip("\n")
    print(number)
    matcher=re.fullmatch(x, number)
if matcher!=None:
        print(num)