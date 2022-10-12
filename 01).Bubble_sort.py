l=[25,40,15,20,5]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
    
    
print(l)

#------------------------------------
#bubble sort when list is in ascending order
l=[1,2,3,4,5]
n=len(l)
f=0
c=0
for i in range(n):
    for j in range(n-i-1):
        c+=1
        if(l[j]>l[j+1]):
            l[j+1],l[j]=l[j],l[j+1]
            f=1
            
    if(f==0):
        break
    
print(l,c)
