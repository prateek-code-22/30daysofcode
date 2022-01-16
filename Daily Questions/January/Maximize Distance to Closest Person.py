def solve(seats):

    pre_zero = -1
    suf_zero = -1
    max_zero = -1
    zero = 0


    for i in range(len(seats)):
        if seats[i]==0:
            zero+=1

        else:
            if pre_zero==-1:
                pre_zero = zero
            else:
                max_zero = max(max_zero,zero)

            zero = 0
    suf_zero = zero
    return max(max(pre_zero,suf_zero),(max_zero+1)//2)

    