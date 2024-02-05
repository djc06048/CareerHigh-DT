arr = [1, 2, 1, 3, 1, 4, 1, 2, 1]

ans = [0 for i in range(len(arr))]
visited = [False] * (len(arr))

def dfs(at, depth):
    if depth == 3:
        one = arr[0:ans[0]]
        two = arr[ans[0]:ans[1]]
        three = arr[ans[1]:ans[2]]
        four = arr[ans[2]:]

        checkEquality(one, two, three, four)

        return
    else:
        for i in range(at, 8):
            if not visited[i]:
                visited[i] = True
                ans[depth] = i
                dfs(i, depth + 1)
                visited[i] = False


def checkEquality(one, two, three, four):
    if len(set(one)) == len(set(two)) == len(set(three)) == len(set(four)):
        print(one, two, three, four)
        return True
    return False


dfs(1, 0)

## 멘토님 답

topA = [], topB = [], topC = [], topD = []

temp = [1, 2, 1, 3, 1, 4, 1, 2, 1]
for i in range(1, 7):
    topA = temp[:i]
    for j in range(i + 1, 8):
        topB = temp[i:j]
        for k in range(j + 1, 9):
            topC = temp[j:k]
            topD = temp[k:]
            if len(set(topA)) == len(set(topA)) == len(set(topA)) == len(set(topA)):
                print(topA, topB, topC, topD)
