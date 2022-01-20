import math

def solve(piles,h):

    def isPossible(piles,h,mid):
            total = 0.0
            for pile in piles:
                total += (math.ceil((1.0*pile)/mid))
            if total > h:
                return True
            return False


    start = 1
    end = max(piles)

    while start<=end:
        mid = start + (end-start)//2

        if isPossible(piles,h,mid):
            start = mid+1
        else:
            end = mid-1

    return start


piles = [312884470]
h = 968709470
print(solve(piles,h))