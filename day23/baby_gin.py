import sys
sys.stdin = open('./5203_input.txt')

def is_run(arr):
    unq = list(set(arr))
    for n in unq:
        if arr.count(n) == 3:
            return True
    return False

def is_tri(arr):
    unq = sorted(list(set(arr)))
    for idx in range(len(unq)-2):
        n = unq[idx]
        for sep in range(1, 3):
            if unq[idx+sep] != n + sep:
                break

        else:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    array = list(map(int, input().split()))

    print(f'#{tc}', end = ' ')

    p1 = []
    p2 = []
    for i, num in enumerate(array):
        if i % 2 == 0:
            p1.append(num)
            if i >= 4:
                if is_run(p1) or is_tri(p1):
                    print(1)
                    break
        else:
            p2.append(num)
            if i >= 4:
                if is_run(p2) or is_tri(p2):
                    print(2)
                    break

    else:
        print(0)

