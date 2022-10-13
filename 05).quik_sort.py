#quicksort
def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        print(alist[p]) 
        quicksort(alist, start, p) #left part
        quicksort(alist, p + 1, end) #right part 
 
 
def partition(alist, start, end):
    pivot = alist[start] #first element as pivot
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot): #setting left part
            i = i + 1
        while (i <= j and alist[j] >= pivot): #setting right part
            j = j - 1
 
        if i <= j: # 
            alist[i], alist[j] = alist[j], alist[i]   
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)
