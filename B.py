from itertools import permutations
for _ in range(int(input())):
    n = int(input())
    cnt = 1
    a = [i for i in range(1,n+1)]
    a.sort(reverse=True)
    print(*a)
    while cnt < n:
        a[0], a[cnt] = a[cnt], a[0]
        print(*a)
        cnt += 1
