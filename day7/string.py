import sys

### 보이어-무어
def search(string, kw):
    count = 0
    kw_len = len(kw)
    idx = kw_len - 1
    skip_dict = {}

    for i, k in enumerate(kw):
        # skip_dict.setdefault(k, idx - i)
        skip_dict[k] = idx - i

    while idx < len(string):
        end = string[idx]
        skip = skip_dict.get(end, kw_len)

        if end == kw[-1]:
            for i in range(1, kw_len):
                idx -= 1
                if kw[-1 - i] != string[idx]:
                    skip = skip_dict.get(string[idx], kw_len)
                    break

            else:
                skip = kw_len
                count += 1


        idx += skip

    return count



sys.stdin = open('./test_input.txt', encoding = 'UTF8')

for _ in range(10):
    tc = input()
    keyword = input()
    words = input()

    result = search(keyword, words)

    print(f'#{tc} {result}')

