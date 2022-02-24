def sub_lists (l, x):
    lists = {}
    for i in range(len(l) + 1):
        for j in range(i):
            ln = len(l[j: i])
            s = sum(l[j:i]) 
            flag = False
            for key, val in lists.items():
                if s + ln * x < val + key * x and ln>key:
                    flag = True
                    break
            if not flag:
                lists[ln] = s
    return lists
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sub = sub_lists(a, x)
    print(sub)
    b = []
    for i in range(n+1):
        best = 0
        for key, val in sub.items():
            if best >= val + key * x:
                continue
            if i>=key:
                v = val + key * x
                if best < v:
                    best = v
            else:
                v = val + i * x
                if best < v:
                    best = v
        b.append(best)
    print(*b)

