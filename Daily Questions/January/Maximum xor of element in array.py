#Approach-1 
# We can do it in O(n^2) by find max xor of each element in array to its rights.

#Approach 2
#using trie data structure
#1. we insert the binary value of each element into trie.
#2. now to maximize the xor we will find the opposite bit in trie.(ex: 0101 -> 1010) if can not find the opposite bit then we will keep orginal bit.



class TrieNode:
    def __init__(self):
        self.child = {}
        
    def increase(self, number):
        cur = self
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child:
                cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            
    def findMax(self, number):
        cur, ans = self, 0
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            else:
                cur = cur.child[bit]
        return ans


class Solution:
    def findMaximumXOR(self, nums):
        trieNode = TrieNode()
        for x in nums:
            trieNode.increase(x)
            
        ans = 0
        for x in nums:
            ans = max(ans, trieNode.findMax(x))
        return ans