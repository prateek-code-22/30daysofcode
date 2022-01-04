def bitwiseComplement(n):
        
        if n==0:
            return 1
        
        i = 1
        
        while i <= n:
            i = i << 1
            
        return (i - 1) ^ n
