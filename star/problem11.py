def tree(num):
    if num == 3:
        result = '  *  \n' + ' * * \n' + '*****'
        return result
    
    div_2 = int(num / 2)
    small_tree = tree(div_2)
    part1 = ''
    part2 = ''
    
    ### part1
    for line in small_tree.split('\n'):
        part1 += (' ' * div_2) + line + (' ' * div_2) + '\n'

    ### part2
    for line in small_tree.split('\n'):
        part2 += line + ' ' + line + '\n'

    result = part1 + part2.strip('\n')

    return result


number = int(input())
result = tree(number)
print(result)