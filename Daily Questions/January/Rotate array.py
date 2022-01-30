# Approach- 
# We can slice the part of list which is to be rotated k times.


def rotate(arr,k):
    
    # length of list(arr)
    n = len(arr)
    # no of rotation which is to be performed on list. 
    k = k % n

    #slicing in python s[x,y] , x is included and y is excluded.
    #arr[:] => is used to modify inplace list(arr)
    #arr[n-k:] => to get subarray which is not to be rotated (is placed first)
    #arr[:n-k] => elements to be rotated from indx(0 to k) is placed at last.
    arr[:] = arr[n-k:] + arr[:n-k] 

