arr = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]

def roll(lst, count = 0):
    result = []
    if not lst:
        return result

    if count % 4 == 0:
        for num in lst.pop(0):
            result.append(num)

        count += 1
        result.extend(roll(lst, count))

    elif count % 4 == 1:
        for l in lst:
            result.append(l.pop())

        count += 1
        result.extend(roll(lst, count))

    elif count % 4 == 2:
        for num in lst.pop()[::-1]:
            result.append(num)

        count += 1
        result.extend(roll(lst, count))

    elif count % 4 == 3:
        for l in lst:
            result.append(l.pop(0))

        count += 1
        result.extend(roll(lst, count))

    return result

ans = roll(arr)

for i in ans:
    print(i)