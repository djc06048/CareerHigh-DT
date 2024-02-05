def wyw(idx):
    answer = []
    num = 0
    while (True):
        num = str(num)

        if len(num) % 2 == 0:
            left = num[0:len(num) // 2]
            right = num[len(num) // 2:]
            if left == right:
                answer.append(num)
        else:
            left = num[0:len(num) // 2]
            right = num[len(num) // 2 + 1:]
            if left == right:
                answer.append(num)

        if len(answer) == idx:
            break
        num=int(num) +1

    print(answer[idx-1])
    return answer[idx-1]


wyw(100)
