# This problem can be solved using Trie data structure.

#structure of Trie
class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    # add character in trie.    
    def add(self,word):
        cur = self.root

        #for each letter in word if not present create new node.
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
        #if already present
            cur = cur.children[c] 
        cur.word = True

    def search(word):
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                
                #if char is '.'
                if c==".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                
                #if char is not '.' then search in trie and return res (T/F)
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0,self.root)

