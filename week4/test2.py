def solution(arr):
    ans=list()

    for i in range(len(arr)-1):
        flag =False
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                flag=True
                ans.append(arr[j])
                break

        if not flag:
            ans.append(-1)

    ans.append(-1)
    print(ans)

solution([9,1,5,3,6,2])
solution([2,3,3,5])


## 멘토님 답
temp=[9,1,5,3,6,2]
res=[]
for ii,i in enumerate(temp):
    for jj,j in enumerate(temp[ii+1:]):
        if j>i:
            res.append(j)
            break
        if jj==len(temp[ii+1:])-1:
            res.append(-1)
res.append(-1)
