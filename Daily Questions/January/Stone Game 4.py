#basic intution is if completely divisible by perfect square then alice wins and if 0 is left then bob wins.



def solve(n):
        
        dp = [False]*(n+1)
        
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if dp[i-k*k] == False:
                    dp[i] = True
                    break
        
        return dp[n]
    
n = 3
print(solve(n))
