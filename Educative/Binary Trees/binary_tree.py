class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return f"{self.data}"
def parse_binary_tree(tree):
    if tree!=None:
        print(tree.data)
        parse_binary_tree(tree.left)
        parse_binary_tree(tree.right)
def check_identical(tree1,tree2):
    root=tree1
    root2=tree2
    print(root,root2)
    if root==None and root2==None:
        return True
    if root!=None and root2!=None:
        return root.data==root2.data and (check_identical(root.left,root2.left),check_identical(root.right,root2.right))
    return False
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print (root.data)
        print_inorder(root.right)
def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.data)
if __name__=="__main__":
    root=Node(100)
    root.left=Node(50)
    root.right=Node(200)
    root.left.left=Node(25)
    root.right.left=Node(125)
    root.right.right=Node(350)
    # parse_binary_tree(root)
    root1=Node(100)
    root1.left=Node(50)
    root1.right=Node(200)
    root1.left.right=Node(25)
    root1.right.left=Node(125)
    root1.right.right=Node(350)
    a=print_inorder(root)
