def box(num):
    result = ''

    if num == 3:
        result = '***\n' + '* *\n' + '***'

        return result
    
    small_box = box(num / 3)

    for i in range(3):
        for line in small_box.split('\n'):
            if i != 1:
                result += line * 3 + '\n' 

            else:
                result += line + ' ' * len(line) + line + '\n'

    result = result.strip('\n')

    return result


number = int(input())
result = box(number)
print(result)
                    