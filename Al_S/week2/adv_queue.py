import sys
# from collections import deque
from queue import Queue

def adv(l, n, arr):
    arr_len = 2*n
    max_time = 0

    que = Queue()

    ad_time = 0
    abs_tsum = 0

    for i in range(arr_len - 1):
        if i % 2 == 0:
            diff = arr[i + 1] - arr[i]
            ad_time += diff
            abs_tsum += diff
            que.put(diff)
            tmp_ad = ad_time

            while abs_tsum > l:
                bottom = que.get()
                diff2 = abs_tsum - l
                abs_tsum -= abs(bottom)

                if diff2 >= abs(bottom) and bottom > 0:
                    ad_time -= bottom
                    tmp_ad -= bottom

                elif diff2 < bottom:
                    ad_time -= bottom
                    tmp_ad -= diff2

        else:
            diff = arr[i] - arr[i + 1]
            abs_tsum += diff * (-1)
            que.put(diff)
            tmp_ad = ad_time

            while abs_tsum > l:
                bottom = que.get()
                diff2 = abs_tsum - l
                abs_tsum -= abs(bottom)

                if diff2 >= abs(bottom) and bottom > 0:
                    ad_time -= bottom
                    tmp_ad -= bottom

                elif diff2 < bottom:
                    ad_time -= bottom
                    tmp_ad -= diff2

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
