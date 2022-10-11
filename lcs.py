def lcs(i,j):
    if(i==len(s1) or j==len(s2)):
        return 0
    elif(s1[i]==s2[j]):
        return 1+lcs(i+1,j+1)
    else:
        return max(lcs(i,j+1),lcs(i+1,j))
global s1,s2
s1='sairam'
s2='saikrishna'
print(lcs(0,0))
