l=[25,40,15,20,5]
for i in range(len(l)):
    min=i
    for j in range(i+1,len(l)):
        if(l[min]>=l[j]):
            min=j 
    l[i],l[min]=l[min],l[i]
        
        
 # finding minimum value index and swap with starting index
# 1st element will smallest,next smallest
    
print(l)

#------------------------------------------
#selection sort when list is in ascending order
l=[5,3,8,5,1,9,4]
n=len(l)
f=0
c=0
for i in range(n):
    for j in range(i+1,n):
        c+=1
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
            #c+=1
        if(l[j]<l[j-1]):
            f=1
            
    if(f==0):
        break
    
print(l,c)
