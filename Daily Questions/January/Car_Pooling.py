#Approach -1 

#Step1 : create a auxilary array and initalize with zero.
#Step2 : update the value of aux array.
# the pickup point tell how many passenger will occupy the seat in car.
# drop point tell the seats are vacant. 
# Step3 :calculate the prefix sum of aux array and check if sum is greator than capacity then return false.


#So at pick up point add the No of passenger in aux array. and at drop point substract the passenger count.
#in this aux: [0,2,0,3,0,-2,0,-3,0,0,0,0,...  ]
# index:      [0,1,2,3,4, 5 ,6, 7 ,8,9... ..101]

#edge case: IF at the same index some passengers are dropped and some of them are pickup then store the final res value of that index. 
#example: at particular index, -3 are dropped and 2 are pick up then result to that index is -3+2 = -1

#TC - O(N)
#SC - O(N)

def pool(nums,capacity):
    total_passenger = 0
    aux = [0]*1001
    n = len(aux)

    for ele in nums:
        aux[ele[1]] += ele[0]
        aux[ele[2]] += -(ele[0])
    
    for i in range(n):
        total_passenger += aux[i]

        if total_passenger>capacity:
            return False

    return True

nums = [[2,1,5],[3,3,7]]
print(pool(nums,5))
