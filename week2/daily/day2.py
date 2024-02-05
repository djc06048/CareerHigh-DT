def cheeckGenerator():
    check = [False] * 5001
    for i in range(1, 5001):
        sum = 0
        numlist = []
        for j in list(map(int, str(i))):
            numlist.append(j)
        numlist.append(i)
        for j in numlist:
            sum=sum+int(j)
        if(sum<=5000):
            check[sum]=True
    return check
def getSumOfSelfNumber(selfnumlist):
    for idx,target in enumerate(selfnumlist):
        if(target==False):
            print(idx)
            ans=ans+idx
    return ans

selfnumlist=cheeckGenerator()
print(getSumOfSelfNumber(selfnumlist))
