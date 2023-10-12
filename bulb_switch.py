N = int(input())
before = list(map(int, input()))
after = list(map(int, input()))
cnt1 = 0
cnt2 = 1
inf = 1e9
ans = inf

case1 = before[:]
case2 = before[:]
case2[0] = (case2[0] + 1) % 2
case2[1] = (case2[1] + 1) % 2

for i in range(1, N):
    if case1[i-1] != after[i-1]:
        cnt1 += 1
        case1[i] = (case1[i] + 1) % 2
        case1[i-1] = (case1[i-1] + 1) % 2

        if i + 1 != N:
            case1[i+1] = (case1[i+1] + 1) % 2

for i in range(1, N):
    if case2[i-1] != after[i-1]:
        cnt2 += 1
        case2[i] = (case2[i] + 1) % 2

        case2[i-1] = (case2[i-1] + 1) % 2

        if i + 1 != N:
            case2[i+1] = (case2[i+1] + 1) % 2

if case1 == after:
    ans = min(ans, cnt1)

if case2 == after:
    ans = min(ans, cnt2)

if ans == inf:
    print(-1)

else:
    print(ans)