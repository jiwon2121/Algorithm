class Solution:
    inf = 1e9

    def minOperations(self, nums, x) -> int:
        if sum(nums) < x:
            return -1
        self.N = len(nums)
        self.dp = {}
        self.all_use = (1 << self.N) - 1
        self.x = x
        self.nums = nums
        ans = self.oper()
        if ans != Solution.inf:
            return ans

        return -1

    def oper(self, used=0, left=0, right=0, total=0):
        if total == self.x:
            return 0

        elif total > self.x:
            return Solution.inf

        elif used == self.all_use:
            return Solution.inf

        if used in self.dp:
            return self.dp[used]

        temp = Solution.inf
        if not used & 1 << left:
            cnt = self.oper(used | 1 << left, left+1, right, total + self.nums[left])
            if cnt != Solution.inf:
                temp = min(temp, cnt + 1)

        if not used & (1 << self.N - 1 - right):
            cnt = self.oper(used | (1 << self.N - 1 - right), left, right+1, total + self.nums[self.N - 1 - right])
            temp = min(temp, cnt + 1)

        self.dp[used] = temp

        return temp

# p1 = [5,6,7,8,9]
# p2 = 4
p1 = [6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119]
p2 = 31841
sol = Solution()
print(sol.minOperations(p1, p2))
print(sol.dp[0])
b = f'{295444:b}'
test = 0
for i in range(len(p1)):
    if 295444 & 1 << i:
        print(p1[i])
        test += p1[i]

print(test)