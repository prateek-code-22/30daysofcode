def largestRectangleArea(arr):
    n = len(arr)
    stack = []
    maxArea = 0

    for i in range(0,n+1):
        while len(stack)!=0 and (i==n or arr[stack[-1]]>=arr[i]):
            #can be the possible height of rectangle
            height = arr[stack[i]]
            stack.pop()

            #if stack is empty consider ith index as width
            if len(stack)==0:
                width = i 
            #else calc width by substracting current index -left most index - 1 
            else:
                width = i - stack[-1] - 1
            
            #calc possile area for rectangle
            maxArea = max(maxArea,height*width)
        stack.append(i)

    return maxArea