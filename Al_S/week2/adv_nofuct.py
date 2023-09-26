import sys
import time

sys.stdin = open('./2_input.txt')

start = time.time()
T = int(input())
que = [None for _ in range(200000)]
array = [0 for _ in range(200000)]

for tc in range(1, T+1):
    L = int(input())
    N = int(input())
    for i in range(N):
        array[2 * i], array[2 * i + 1] = map(int, input().split())


    arr_len = 2*N
    max_time = 0

    bottom = 0
    top = -1

    ad_time = 0
    abs_tsum = 0

    for i in range(arr_len - 1):
        if i % 2 == 0:
            diff = array[i + 1] - array[i]
            ad_time += diff
            abs_tsum += diff
            top += 1
            que[top] = diff
            tmp_ad = ad_time

            while abs_tsum > L:
                diff2 = abs_tsum - L
                abs_tsum -= abs(que[bottom])

                if diff2 >= abs(que[bottom]) and que[bottom] > 0:
                    ad_time -= que[bottom]
                    tmp_ad -= que[bottom]

                elif diff2 < que[bottom]:
                    ad_time -= que[bottom]
                    tmp_ad -= diff2

                bottom += 1

        else:
            diff = array[i] - array[i + 1]
            abs_tsum += diff * (-1)
            top += 1
            que[top] = diff
            tmp_ad = ad_time

            while abs_tsum > L:
                diff2 = abs_tsum - L
                abs_tsum -= abs(que[bottom])

                if diff2 >= abs(que[bottom]) and que[bottom] > 0:
                    ad_time -= que[bottom]
                    tmp_ad -= que[bottom]

                elif diff2 < que[bottom]:
                    ad_time -= que[bottom]
                    tmp_ad -= diff2

                bottom += 1

        if max_time < tmp_ad:
            max_time = tmp_ad



    # result = adv(L, N, arr)
    print(f'#{tc} {max_time}')

print(time.time() - start)