def find_minimum(arr):
    # Write your code here
    least_value=None
    for i in arr:
        if least_value==None:
            least_value=i
        else:
            if i<=least_value:
                least_value=i
    return least_value

if __name__=="__main__":
    print(find_minimum([9, -1, 3, 6]))
