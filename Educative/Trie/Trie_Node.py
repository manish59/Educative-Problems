class TrieNode:
    def __init__(self,char):
        self.char=char
        self.children={}
        self.is_end_word=False
    def mark_as_left(self):
        self.is_end_word=True
    def unmark_as_leaf(self):
        self.is_end_word=False
class Trie:
    def __init__(self):
        self.root=TrieNode(None)
    def get_root_children(self):
        return self.root.children
    def add_node(self,word):
        current=self.root
        for i in word:
            if i in current.children:
                current=current.children[i]
            else:
                current.children[i]=TrieNode(i)
                # print(current.children,i)
                current=current.children[i]

        current.mark_as_left()
def print_trie(tree,result=""):
    root=None
    if 'root' in tree.__dict__:
        root=tree.root
    else:
        root=tree
    children=root.children
    for i in children:
        if not children[i].is_end_word:
            print_trie(children[i],result+i)
        else:
            result +=i
            print(result)
def get_suggestions(trie,word,suggestions=""):
    root=None
    if 'root' in trie.__dict__:
        root=trie.root
    else:
        root=trie
    children=root.children
    for i in word:
        if i in children and not children[i].is_end_word:
            suggestions=suggestions+i
            

if __name__=="__main__":
    trie=Trie()
    # print(trie.get_root().char)
    trie.add_node("Manish")
    # print(trie.root.children)
    trie.add_node("Makan")
    trie.add_node("Kumar")
    trie.add_node("Whatsup!")
    print_trie(trie)

