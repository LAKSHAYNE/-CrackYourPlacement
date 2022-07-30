def contains(root,i):
    return root.children[ord(i)-ord('a')] !=None
#Function to insert string into TRIE.
def insert(root,key):
    for i in key:
        if(not contains(root,i)):
            root.children[ord(i)-ord('a')]=TrieNode()
        root=root.children[ord(i)-ord('a')]
    root.isEndOfWord=True
    #code here

#Function to use TRIE data structure and search the given string.
def search(root, key):
    for i in key:
        if(not contains(root,i)):
            return 0
        root=root.children[ord(i)-ord('a')]
    return 1 if(root.isEndOfWord) else 0
    #code here