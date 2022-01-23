# Approach :


def seqDigit(low,high):
    
    res = []

    def solve(low,high,i,num):
        #append only valid number
        if num>=low and num<=high:
            res.append(num)
        
        #if num is out of range
        if num>high or i>9:
            return
        
        solve(low,high,i+1,num*10+i)    
    
    num = 0
    #create all possible sequencial number with digit 1-9
    for i in range(1,10):
        solve(low,high,i,num)
    
    res.sort()
    return res

    
low = 100
high = 300
print(seqDigit(low,high))