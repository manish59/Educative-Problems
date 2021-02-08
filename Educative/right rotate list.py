def right_rotate(lst, k):
    # Write your code here
    print(lst)
    total_length=len(lst)-1
    for i in range(k):
        lst.insert(0,lst.pop())
        total_length=total_length-1
    return(lst)
right_rotate([10,20,30,40,50],3)