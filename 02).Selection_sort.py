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
