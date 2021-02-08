"""
To solve happy number problem we can use floyd cyccle detection algorithm like using two pointers fast pointer and slow pointer
here time complexity will be O(number) and space in constant time.
another way is to use dynamic programming and solve the problem by having the results sotred in a dictionary
"""
def happy_number(original_number,calculated_number=[]):
    sum=0
    print(calculated_number)
    calculated_number.append(original_number)
    while(original_number>=1):
        digit=original_number%10
        sum=sum+digit*digit
        original_number=original_number//10
    print(sum)
    if sum==1:
        print("Happy Number")
        return True
    elif sum in calculated_number:
        print("Not a happy number")
        return False
    else:
        happy_number(sum,calculated_number)
if __name__=="__main__":
    happy_number(99)