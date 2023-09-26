import sys

### 보이어-무어
# def search(string, kw):
#     count = 0
#     kw_len = len(kw)
#     idx = kw_len - 1
#     skip_dict = {}
#
#     for i, k in enumerate(kw):
#         # skip_dict.setdefault(k, idx - i)
#         if idx - i == 0:
#             skip_dict.setdefault(k, idx - i)
#         else:
#             skip_dict[k] = idx - i
#     print(skip_dict)
#     while idx < len(string):
#         end = string[idx]
#         skip = skip_dict.get(end, kw_len)
#
#         if end == kw[-1]:
#             for i in range(1, kw_len):
#                 idx -= 1
#                 if kw[-1 - i] != string[idx]:
#                     skip = skip_dict.get(string[idx], kw_len)
#                     break
#
#             else:
#                 skip = kw_len*2 -1
#                 count += 1
#
#         idx += skip
#         print(idx)
#     return count


def search(string, kw):
    idx = 0
    count = 0
    while idx < len(string)-(len(kw)-1):
        for i in range(len(kw)):
            if string[idx + i] != kw[i]:
                idx += 1
                break
        else:
            idx += len(kw) - 1
            count += 1

    return count

def typing(string, kw):
    count = search(string,kw)

    ans = len(string) - (len(kw) - 1) * count

    return ans


sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    word, keyword = input().split()

    result = typing(word, keyword)

    print(f'#{tc} {result}')

