def storm(num):
    if num == 1:
        return '*'
    
    if num == 2:
        result = '*****\n' +\
                 '*    \n' +\
                 '* ***\n' +\
                 '* * *\n' +\
                 '* * *\n' +\
                 '*   *\n' +\
                 '*****'
        
        return result
    
    width = 4 * (num - 1) + 1
    inner_storm = storm(num - 1)

    part1 = '*' * width + '\n'
    part2 = '*' + ' ' * (width-1) + '\n'
    part3 = ''
    part4 = '*' + ' ' * (width-2) + '*' + '\n'

    for i, line in enumerate(inner_storm.split('\n')):
        if i != 0:
            part3 += '* ' + line + ' *\n'

        else:
            part3 += '* ' + line + '**\n'

    result = part1 + part2 + part3 + part4 + part1.strip('\n')

    return result


number = int(input())
storm1 = storm(number)
print(storm1)
