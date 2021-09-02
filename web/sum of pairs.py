lst=[1,2,3,4,5]
low=0
upp=len(lst)-1
pair=6
pairs=[]
while(low<upp):#o(n)
     sum=lst[low]+lst[upp]
     if(sum==pair):

         pairs.append((lst[low],lst[upp]))
         low+=1
     elif(sum>pair):
         upp-=1
     elif(sum<pair):
         low+=1
print(pairs)
#for i in lst:

