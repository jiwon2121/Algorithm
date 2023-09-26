import sys
# import time
def adv(l, n, arr):
    arr_len = 2*n
    max_time = 0

    que = [None for _ in range(arr_len)]
    bottom = 0
    top = -1

    ad_time = 0
    abs_tsum = 0

    for i in range(arr_len - 1):
        if i % 2 == 0:
            diff = arr[i + 1] - arr[i]
            ad_time += diff
            abs_tsum += diff
            top += 1
            que[top] = diff
            tmp_ad = ad_time

            while abs_tsum > l:
                diff2 = abs_tsum - l
                abs_tsum -= abs(que[bottom])

                if diff2 >= abs(que[bottom]) and que[bottom] > 0:
                    ad_time -= que[bottom]
                    tmp_ad -= que[bottom]

                elif diff2 < que[bottom]:
                    ad_time -= que[bottom]
                    tmp_ad -= diff2

                bottom += 1

        else:
            diff = arr[i] - arr[i + 1]
            abs_tsum += diff * (-1)
            top += 1
            que[top] = diff
            tmp_ad = ad_time

            while abs_tsum > l:
                diff2 = abs_tsum - l
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

    return max_time

sys.stdin = open('./2_input.txt')

# start =time.time()
T = int(input())

for tc in range(1, T+1):
    L = int(input())
    N = int(input())
    array = []
    for _ in range(N):
        array.extend(list(map(int, input().split())))

    result = adv(L, N, array)
    print(f'#{tc} {result}')

# print(time.time() - start)