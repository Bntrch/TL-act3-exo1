def symitric(L):
    r=[]
    i=0
    j=-1
    for i in range (len(L)):
        x=L[i]
        y=L[j]
        #r.append(L[i])
        r.append(L[j])
        i = i + 1
        j = j - 1
    return r
L=[1,2,5,7,9,8,6,4,2]
res=symitric(L)
print(L)
print(res)