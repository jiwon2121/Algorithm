def removeKdigits(num: str, k: int) -> str:
    ### 모두 제거되는 케이스
    if len(num) == k:
        return '0'

    ### 정상 케이스
    new_digits = num[0]

    i = 1

    while i < len(num) and k > 0:
        ### 빈 문자열일때 indexerror가 나지 않게 pass
        if not new_digits:
            pass

        elif int(new_digits[-1]) > int(num[i]):
            new_digits = new_digits[:-1]
            k -= 1
            continue

        new_digits += num[i]
        i += 1

    new_digits += num[i:]

    if k > 0:
        new_digits = new_digits[:-k]

    ### 0 제거
    new_digits = new_digits.lstrip('0')

    ### '000' 일때 위에서 모두 제거되어 확인후 return '0'
    if not new_digits:
        return '0'

    return new_digits