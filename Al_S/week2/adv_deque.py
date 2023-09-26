import sys
from collections import deque

def adv(l, n, arr):
    arr_len = 2*n
    max_time = 0

    deq = deque()

    ad_time = 0
    abs_tsum = 0

    for i in range(arr_len - 1):
        if i % 2 == 0:
            diff = arr[i + 1] - arr[i]
            ad_time += diff
            abs_tsum += diff
            deq.append(diff)
            tmp_ad = ad_time

            while abs_tsum > l:
                diff2 = abs_tsum - l
                abs_tsum -= abs(deq[0])

                if diff2 >= abs(deq[0]) and deq[0] > 0:
                    ad_time -= deq[0]
                    tmp_ad -= deq[0]

                elif diff2 < deq[0]:
                    ad_time -= deq[0]
                    tmp_ad -= diff2

                deq.popleft()

        else:
            diff = arr[i] - arr[i + 1]
            abs_tsum += diff * (-1)
            deq.append(diff)
            tmp_ad = ad_time

            while abs_tsum > l:
                diff2 = abs_tsum - l
                abs_tsum -= abs(deq[0])

                if diff2 >= abs(deq[0]) and deq[0] > 0:
                    ad_time -= deq[0]
                    tmp_ad -= deq[0]

                elif diff2 < deq[0]:
                    ad_time -= deq[0]
                    tmp_ad -= diff2

                deq.popleft()

        if max_time < tmp_ad:
            max_time = tmp_ad

    return max_time

sys.stdin = open('./2_input.txt')

T = int(input())

for tc in range(1, T+1):
    L = int(input())
    N = int(input())
    array = []
    for _ in range(N):
        array.extend(list(map(int, input().split())))

    result = adv(L, N, array)
    print(f'#{tc} {result}')
