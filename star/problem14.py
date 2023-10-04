def make_x(num):
    if  num == 0:
        return '*'

    element = make_x(num - 1)
    part1 = ''
    part2 = ''

    for line in element.split('\n'):
        part1 += line + (' ' *len(line)) + line + '\n'

    for line in element.split('\n'):
        part2 += (' ' *len(line)) + line + (' ' *len(line)) + '\n'

    result = part1 + part2 + part1.strip('\n')

    return result


number = int(input())
x = make_x(number)
print(x)