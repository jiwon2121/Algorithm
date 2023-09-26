import sys
sys.stdin = open('./5177_input.txt')

def bin_heap(arr):
    heap = [0]
    i = 0
    for a in arr:
        heap.append(a)
        i += 1
        i2 = i
        while i2 > 1:
            p_idx = i2 // 2
            if heap[i2] < heap[p_idx]:
                heap[i2], heap[p_idx] = heap[p_idx], heap[i2]
                i2 //= 2
            else:
                break

    result = 0
    while i > 1:
        i //= 2
        result += heap[i]

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))

    ans = bin_heap(array)

    print(f'#{tc} {ans}')