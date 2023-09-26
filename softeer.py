def is_right(string):
    cnt = 1
    alp = string[0]
    for i in range(1, n):
        if string[i] != alp:
            if cnt < k:
                return False
            cnt = 1
            alp = string[i]
        
        else:
            cnt += 1
    if cnt < k:
        return False
    
    return True


def solution(string, changed = 0):
    if is_right(string):
        return 0
    
    if string in dp:
        return dp[string]
    
    temp = 2000
    for i in range(n):
        for d in range(-1, 2, 2):
            ni = i + d
            if 0 <= ni < n and not changed & 1 << i and string[i] != string[ni]:
                temp = min(temp, solution(string[:i] + string[ni] + string[i+1:], changed | 1 << i) + 1)

    dp[string] = temp
    return temp

n, k = map(int, input().split())
S = input()
dp = {}
print(solution(S))
print(dp)


    