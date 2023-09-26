def solution(alc):
    acid = []

    for _ in range(len(alc)):  ### 절대값이 큰 수 -> 작은 수
        if alc[-1] > 0:
            acid.append(alc.pop())
        else:
            break

    i = len(acid) - 1
    j = len(alc) - 1

    if i == - 1:
        return sorted([alc[-1], alc[-2]])

    elif j == - 1:
        return sorted([acid[-1], acid[-2]])

    ac = acid.pop()
    al = alc.pop()

    arr = []
    point = 0

    while True:
        if ac + al < 0:
            if point == 1:
                arr[-1].append(ac)
            else:
                arr.append([ac])
            i -= 1
            point = 1

            if i < 0:
                arr.append([al])
                arr[-1].extend(alc[::-1])
                break

            ac = acid.pop()

        elif ac + al > 0 :
            if point == -1:
                arr[-1].append(al)
            else:
                arr.append([al])
            j -= 1
            point = -1

            if j < 0:
                arr.append([ac])
                arr[-1].extend(acid[::-1])
                break

            al = alc.pop()

        else:
            return [al, ac]

    min_diff = 1000000000

    for idx in range(len(arr) - 1):
        sol1 = arr[idx][-1]
        sol2 = arr[idx + 1][0]
        diff = abs(sol1 + sol2)

        if min_diff >= diff:
            min_diff = diff
            result = sorted([sol1, sol2])

        if diff == 0:
            return result

    if len(arr[0]) >= 2:
        sol1 = arr[0][0]
        sol2 = arr[0][1]
        diff = abs(sol1 + sol2)

        if min_diff >= diff:
            min_diff = diff
            result = sorted([sol1, sol2])

    return result


N = int(input())
sols = list(map(int, input().split()))
ans = solution(sols)

print(*ans)

