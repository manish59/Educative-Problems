def maximum_sublist(array):
    current_max=0
    global_max=0
    for i in array:
        print(current_max, global_max)
        if current_max<0:
            current_max=i
        else:
            current_max=current_max+i
        if global_max<current_max:
            global_max=current_max
        print(current_max,global_max)
    return global_max

lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print(maximum_sublist(lst))