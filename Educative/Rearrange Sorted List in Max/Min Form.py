def max_min(lst):
    result=[]
    i=0
    j=len(lst)-1
    while(i<len(lst)/2):
        result.append(lst[j])
        result.append(lst[i])
        i=i+1
        j=j-1
        print(i,j)
        print(result)
    return result
print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))