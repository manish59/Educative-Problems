def remove_even(l):
    return [i for i in l if i%2!=0]

if __name__=="__main__":
    l=[1,4,5,6,4,3,5,6,5,3]
    print(remove_even(l))