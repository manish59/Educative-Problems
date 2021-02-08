def merge_lists(lst1, lst2):
    i=0
    j=0
    result=[]
    while(i<len(lst1) and j<len(lst2)):
        if lst1[i]<=lst2[j]:
            result.append(lst1[i])
            i=i+1
        else:
            result.append(lst2[j])
            j=j+1
    if i<len(lst1):
        result=result+lst1[i:]
    else:
        result=result+lst2[j:]
    return result
def merge_list_inplace(lst1,lst2):
    i=0
    j=0
    while(i<len(lst1) and j<(len(lst2))):
        if lst1[i]>lst2[j]:
            lst1.insert(i,lst2[j])
            j=j+1
            i=i+1
        else:
            i=i+1
    if j<len(lst2):
        lst1.extend(list2[j:])
    return lst1
if __name__=="__main__":
    list1 = [1, 3, 4, 5,6,7,8,9,10,11]
    list2 = [2, 6, 7, 8,9,10]
    print(merge_lists(list1,list2))
    print(merge_list_inplace(list1,list2))