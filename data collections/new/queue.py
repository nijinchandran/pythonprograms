que=[]
size=int(input("enter the size::"))
front=0
rear=0
n=0

def isert():
    global front,rear,size,que
    if rear < size:
        p=int(input("enter the element want to insert::))
        que.insert(rear,p)
        #insert(position,element)
        rear+=1

        for i in range(front,rear):
            print(que,[i])
        else:
     print("que is full")


while n!=1:
    print("enter the operation want to perform")
    opt=int(input("press \n1)enqueue\n2)dequeue\n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()
