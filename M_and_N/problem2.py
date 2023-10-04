def N_and_M(n_lst, m):
    array = []

    if m == 1:
        for lst in n_lst:
            array.append([lst])
        return array

    for i in range(len(n_lst)):
        copied = n_lst[i:]

        if len(copied) < m:
            break

        number = copied.pop(0)
        inner_lst = N_and_M(copied, m - 1)

        for lst in inner_lst:
            temp = [number]
            temp.extend(lst)
            array.append(temp)

    return array


N, M = list(map(int, input().split()))
N_lst = [x + 1 for x in range(N)]

result = N_and_M(N_lst, M)
for r in result:
    print(*r, sep = ' ')