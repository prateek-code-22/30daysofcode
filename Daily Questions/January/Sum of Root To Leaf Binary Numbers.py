def solution(root):

    #to store all numbers in int format
    res = []

    def getSum(root,sumz):

        #if root is empty
        if root==None:
            return 

        #add binary data as string 
        sumz += str(root.val)

        #if leaf node then append it to the res list
        if root.left ==None and root.right==None:
            res.append(int(root.val,2))

        #call for left and right sub tree
        getSum(root.left,sumz)
        getSum(root.right,sumz)
        
        # return sum of whole list
        return sum(res)

    #call the function
    return getSum(root,"")

    
