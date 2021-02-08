def find_product(lst):
    result=[]
    for i in lst:
        product_result=1
        for j in lst:
            if j==i:
                continue
            else:
                product_result *=j
        result.append(product_result)
    return result
def find_product_optimized(lst):
    print("Normal List:",lst)
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    print("Left Product:",product)
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]
        print("Right:",right,"Product",product)

    return product
def find_product(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        print("currentproduct",currentproduct)
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        print("result",result)
        # Updating `left`
        left = left * lst[i]
        print("left",left)
    return result



if __name__=="__main__":
    # print(find_product([4, 2, 3, 4]))
    # print(find_product(lst=[1,2,3,4]))
    print(find_product_optimized([1,2,3,4]))
