
def plant(flowerbed,n):

    f = [0] + flowerbed+ [0]
    #f = [0,1,0,0,0,1,0]
    for i in range(1,n-1):
        if f[i]==0 and f[i-1]==0 and f[i+1]==0:
            
            #plant 
            f[i] = 1
            
            #count of flower to plant is reduced by 1
            n-=1 

    return n<=0


flowerbed = [1,0,0,0,1]
print(plant(flowerbed,1))

