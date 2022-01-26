'''
Algorithm:
By the property of binary search tree we know that left subtree value is less than root value and right subtree value is greater than root value.
so we can use the Inorder traversal to store the root values in list and use Merge function to merge the root values in sorted order in final list.
'''
def getAllElement(root1,root2):
    def dfs(root):
        if root==None:
            return []
            
        left = dfs(root.left)
        right= dfs(root.right)
        return left+[root.val]+right
        
	# x & y contain the inorder traversal of both BST.
    x = dfs(root1)
    y = dfs(root2)
        
	# Merge function to add in final result list.
    i,j = 0,0
    res = []
        
    while i<len(x) and j<len(y):
        if x[i]<y[j]:
            res.append(x[i])
            i+=1
        else:
            res.append(y[j])
            j +=1
                
    while i<len(x):
        res.append(x[i])
        i+=1
        
    while j<len(y):
        res.append(y[j])
        j +=1
            
    return res
