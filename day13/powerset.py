import sys

sys.stdin = open('./input2.txt', encoding = 'utf8')


def powerset(n, arr, col = 0, total = 0):
    global count
    if col == n:
        return

    powerset(n, arr, col+1, total)

    num = arr[col]
    if total + num == 10:
        count += 1

    elif total + num > 10:
        return

    else:
        powerset(n, arr, col+1, total+num)

array = list(map(int, input().split()))
N = len(array)
count = 0
powerset(N, array)

print(f'#1 {count}')
