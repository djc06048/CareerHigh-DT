import math
def fun1(n):
    return math.sqrt(n)

print(fun1(799))

def fun2(n):
    for i in range(1,n+1):
        if(i*i==n):
            return i
    return -1
print(fun2(799))

for i in range(2000,3000):
    if 799-(i/100)**2<0:
        print(i/100)
        break

def fun3(n):
    for i in range(1,n+1):
        if(i*i==n):
            return True
    return False
print(fun3(26))

def fun4(n):
    count=0
    for k in range(0,n+1):
        if(fun3(k)):
            count=count+1
    return count

print(fun4(1000))
