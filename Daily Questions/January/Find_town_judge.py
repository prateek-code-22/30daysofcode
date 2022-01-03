def findJudge(n,trust):
    #Condition to be judge:
    #1.which do not trust anyone.
    #2.Trusted by all.


    #creating two auxilary array for storing the trust and trusted values.
    #size is n+1 because indexing starts with 1.
    #temp1 stores the trust value(candidate trust how many people).
    #temp2 stores the trusted value(no of people trusting the candidate).

    temp1 = [0] * (n+1)
    temp2 = [0] * (n+1)

    #update the count of trust and trusted value for each candidate.
    for i,j in trust:
        temp1[i] +=1
        temp2[j] +=1

    #check if trust ==0 and trusted by n-1 candidates.
    for i in range(1,n+1):
        if temp1[i]==0 and temp2[i]==n-1:
            return i

    #else return -1 no Judge.
    return -1


arr = [[1,2]]
n = len(arr)
print(findJudge(n,arr))

