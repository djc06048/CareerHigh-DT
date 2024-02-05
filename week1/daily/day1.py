def fun1(n):
    arr=[]
    for i in range(1,n+1):
        if(n%i==0):
            arr.append(i)
    return arr
print(fun1(100))

def fun2(n):
    arr=[]
    for i in range(1,n+1):
        if(n%i==0):
            arr.append(i)
    return len(arr)
print(fun2(20))

def fun3(n):
    visited=[True]*(n+1)
    visited[1]=False
    visited[0]=False
    for i in range(2,n+1):
        for j in range(i*i,n+1,i):
            visited[j]=False
    return visited.count(True)
print(fun3(1000))
