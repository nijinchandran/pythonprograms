lst=[1,2,3,4,5]
pops=int(input("enter index"))
try:
    print(lst[pops])
except Exception as b:
    print(b.args)
