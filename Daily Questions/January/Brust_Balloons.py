# BRUST Balloons
# https://leetcode.com/problems/burst-balloons/



#we have to maximize the coins by brusting the balloons. 
def maxCoins(self, nums):
        
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: 
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): 
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)



