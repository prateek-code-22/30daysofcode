'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

1. arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

        arr = [0,3,2,1]
'''


def validMountainArray(arr):
    #start from index 1
        i = 1
        n = len(arr)
        
        #traverse from index 1 to peak point
        while i<n and arr[i]>arr[i-1]:
            i +=1
        
        #if there is no more element present will reached end or we do not move from starting position.
        if i==1 or i==n:
            return False
        
        #we are at peak point so traverse from peak point to end.
        while i<n and arr[i]<arr[i-1]:
            i +=1
            
        #if it statisfy all condition then return true
        return i==n

        
