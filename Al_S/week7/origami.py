def origami(n=0):
    if n == 2 * k:
        return [[hole]]

    direction = dir_input[n]
    before = origami(n + 1)
    after = []

    for b in before:
        after.append(list(map(lambda x: trans[direction][x], b)))

    if direction == 'D':
        return after[::-1] + before
    elif direction == 'U':
        return before + after[::-1]
    elif direction == 'R':
        for i in range(len(after)):
            after[i].reverse()
            after[i].extend(before[i])
        return after
    elif direction == 'L':
        for i in range(len(before)):
            after[i].reverse()
            before[i].extend(after[i])
        return before

trans = {
    'D' : (2, 3, 0, 1),
    'U' : (2, 3, 0, 1),
    'R' : (1, 0, 3, 2),
    'L' : (1, 0, 3, 2),
}

k = int(input())
k2 = 2 ** k
dir_input = input().split()
hole = int(input())

for o in origami():
    print(*o)
