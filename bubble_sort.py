#Insertion sort
l=[25,40,15,20,5]
for i in range(1,len(l)):
    key=l[i]
    j=i-1  #compare our element with previous element
    while(key<l[j] and j>=0):
        l[j+1]=l[j] #moving forword big element
        j-=1
    l[j+1]=key
    
print(l)
"""
  leave 25
  start with 40
  now key=40
  40<25(j)
  --------
  key=15
  15<40
  now 25,40,40,15,20,5
  nxt,
  15<25
  now 25,25,40,15,20,5
  nxt
  swap j+1 with key
  15,25,40,20,5
  -----------
  now key=20
  .....
