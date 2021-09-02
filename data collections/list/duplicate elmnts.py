a=[1,2,3,5,6,8,9,1,2,3]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)