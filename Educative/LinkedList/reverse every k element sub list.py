class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self):
        self.head=None
    def __repr__(self):
        if self.head==None:
            return "SLL is empty"
        else:
            current=self.head
            string="head"
            while(current.next!=None):
                string=string+"->"+str(current.data)
                current=current.next
            return string
    def printsll(self):
        if self.head==None:
            return "SLL is empty"
        else:
            current=self.head
            string = "head"
            while(current!=None):
                # print(current.data)
                string = string + "->" + str(current.data)
                current=current.next
            print(string)
    def append(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=node
    def add_at_head(self,value):
        node=Node(value)
        node.next=self.head
        self.head=node
def reverse_at_kth_elements(sll,k):
    current=sll.head
    counter=1
    previous=None
    next=None
    new_sll=SingleLinkedList()
    while(current):
        if counter%(k+1)!=0:
            new_sll.add_at_head(current.data)
        else:
            new_sll.append(current.data)
        current=current.next
        counter +=1
        new_sll.printsll()
    return new_sll
if __name__=="__main__":
    sll=SingleLinkedList()
    for i in range(1,10):
        sll.append(i)
    sll.printsll()
    new_sll=reverse_at_kth_elements(sll,3)
    new_sll.printsll()
