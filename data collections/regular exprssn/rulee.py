import re

x= "a{1,3}"
r="aaa abc aaaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())