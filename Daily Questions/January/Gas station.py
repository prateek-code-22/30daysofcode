def gas_Station(gas,cost):
    
    #total gas is less than total cost then it is not possible.
    if sum(gas)<sum(cost):
            return -1
         
    total = 0 
    res = 0 #starting with index 0
        
    for i in range(len(gas)):
        total += (gas[i]-cost[i])        
            
        #if diff between gas and cost is neg then reset total to zero and check for next station
        #it means we cannot move from one station to another station.
        if total<0:
            total = 0
            res = i+1

    return res

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
#starting point will be 3 index.
#diff = [-2,-2,-2,3,3]
print(gas_Station(gas,cost))

