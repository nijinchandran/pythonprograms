k=6
for i in range(6):
    for r in range(k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()