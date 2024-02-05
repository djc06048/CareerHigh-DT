def fun1(n):
    return list(n)

print(fun1("1234"))

def fun3(n):
    count=0
    for i in list(n):
        count=count+int(i)
    return count
print(fun3("1234"))

def fun4(n):
    answer=0
    for i in range(n+1):
        count=0
        for k in list(str(i)):
            count=count+int(k)
        if count%9==0 and i != 0:
            answer=answer+1
    return answer

print(fun4(10000))
