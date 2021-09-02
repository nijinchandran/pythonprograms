lst=[1,6,5,8,7,9,10,11,12,13,14,15,16,17,18,19]
def bsearch():
    lst.sort()
    print(lst)
    ele=int(input("enter the element"))
    fla=0
    low=0
    upp=len(lst)-1
    while low <=upp:
        mid=(low+upp)//2
        if ele >lst[mid]:
            low=mid+1
        elif ele <lst[mid]:
            upp=mid-1
        elif ele==lst[mid]:
            fla=1
            break
    if fla==1:
        print("found")
    else:
        print("not found")

bsearch()
