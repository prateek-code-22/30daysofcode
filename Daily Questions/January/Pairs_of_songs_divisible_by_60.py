#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

#Approach-1: BRUTE FORCE
#TC - O(n^2)

def calculate(time):
  n = len(time)
  count =0 
  
  for i in range(n):
    for j in range(i+1,n):
      if (time[i]+time[j])%60 == 0:
        count +=1
        
    return count


#Approach-2: 
#TC - O(n)
#SC- O(1) or O(60)

def calculate2(time):
    n = len(time)
    res = 0
    #auxilary array for the storing the count.
    count = [0]*60
 
    #count is intialized with 0 so every time before updating the value of index in count we add it to res.
    for ele in range(n):
        index = time[ele] % 60
        res += count[(60 - index)%60]
        count[index] += 1
    return res
