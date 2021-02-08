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
    def __len__(self):
        counter = 0
        if self.head==None:
            return counter
        else:
            current=self.head
            while(current!=None):
                counter+=1
                current=current.next
            return counter
    def insert_at(self,index,value):
        node=Node(value)
        if len(self)>=index:
            current=self.head
            i=0
            while(current.next!=None and i!=index-1):
                current=current.next
                i=i+1
            if current.next==None:
                current.next=node
            else:
                node.next=current.next
                current.next=node
            #[1,2,3,4,5,6,7]
        else:
            print("Not enough elements")
    def search(self,value):
        if self.head==None:
            return False
        current=self.head
        while(current!=None):
            if current.data==value:
                return True
            current=current.next
        return False
    def delete_by_value(self,value):
        if self.search(value):
            current=self.head
            if current.data==value:
                self.head=self.head.next
                return
            while(current.next!=None):
                if current.next.data==value:
                    break
                current=current.next
            if current.next.next==None:
                current.next=None
            else:
                current.next=current.next.next
        else:
            return "Value not present in the linkedlist"
    def reverse(self):
        if self.head==None:
            return
        new_list=SingleLinkedList()
        current=self.head
        while(current!=None):
            new_list.add_at_head(current.data)
            current=current.next
        return new_list
    def reverse_in_place(self):
        current=self.head
        previous=None
        next=None
        # 1->2->3->4
        #next=2
        #current.next=None
        #previous=1
        #current=2
        while current:
            next=current.next
            current.next=previous
            previous=current
            current=next

        self.head=previous
        return
    def find_middle_node(self):
        slow_pointer=self.head
        fast_pointer=self.head
        while(fast_pointer):
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
        return slow_pointer
def detect_loop(sll):
    first_pointer=sll.head
    second_pointer=sll.head
    while first_pointer and second_pointer and second_pointer.next:
        first_pointer=first_pointer.next
        second_pointer=second_pointer.next.next
        if first_pointer==second_pointer:
            return True
    return False
def remove_duplicates(sll):
    values=[]
    current=sll.head
    previous=None
    while(current):
        if current.data in values:
            if previous==None:
                sll.head=current.next
            else:
                previous.next=current.next
        else:
            values.append(current.data)
        previous = current
        current=current.next
    print(values)
    sll.printsll()
if __name__=="__main__":
    sll=SingleLinkedList()
    print(sll)
    sll.append(1)
    sll.append(2)
    sll.append(2)
    sll.append(1)
    sll.add_at_head(0)
    sll.add_at_head(1)
    sll.append(31)
    sll.append(32)
    sll.insert_at(1,100)
    sll.printsll()
    print(len(sll))
    print(sll.search(-1))
    print(sll.delete_by_value(1))
    sll.printsll()
    # sll.reverse_in_place()
    sll.printsll()
    print(sll.find_middle_node())
    remove_duplicates(sll)