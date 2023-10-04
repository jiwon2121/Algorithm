def box(num):
    if num == 1:
        return '*'
    
    width = 1 + 4 * (num - 1)
    inner_box = box(num-1)
    result = ''

    part1 = '*' * width + '\n'
    part2 = '*' + ' ' * (width - 2) + '*' + '\n'
    
    part3 = ''
    for line in inner_box.split('\n'):
        part3 += '*' + f'{line : ^{width-2}}' + '*' + '\n'

    result = part1 + part2 + part3 + part2 + part1.strip('\n')

    return result


number = int(input())
print(box(number))