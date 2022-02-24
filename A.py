for _ in range(int(input())):
    s = input()
    keys = []
    flag = False
    for ch in s:
        if ch.lower() == ch:
            keys.append(ch)
            continue
        else:
            if ch.lower() in keys:
                continue
            else:
                print("NO")
                flag = True
                break
    if not flag:
        print("YES")