def rearrange(lst):
    # Write your code here
    new_list=[]
    for i in lst:
        if i<0:
            new_list.insert(0,i)
        else:
            new_list.insert(len(lst)-1,i)
        print(lst)
    return new_list
print(rearrange([10,-1,20,4,5,-9,-6]))