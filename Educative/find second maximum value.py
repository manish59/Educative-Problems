def find_second_maximum(lst):
    max_value=float('-inf')
    second_max_value=float('-inf')
    # 1,2,3,4,5,6
    for i in lst:
        if i<max_value and i<second_max_value:
            second_max_value=i
        elif i<max_value and i >second_max_value:
            second_max_value=i
        elif i>=max_value:
            second_max_value=max_value
            max_value=i
        print(max_value,second_max_value)
    return second_max_value
print(find_second_maximum([9,2,1,3,4,5,3,2,6,7,5,4,8]))

