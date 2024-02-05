def hanoi(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 3
    else:
        return 1 + hanoi(n - 1) + hanoi(n - 1)
print(hanoi(4))
