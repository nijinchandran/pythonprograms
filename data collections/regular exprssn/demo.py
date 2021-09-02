import re

x="[abc]" #either a b or c
matcher=re.finditer(x,"abt c@5kzabc")
for match in matcher:
    print(match.start())
    print(match.group())
    