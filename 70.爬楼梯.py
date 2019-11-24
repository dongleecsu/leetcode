#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    # 动态规划
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        nums = [0] * n
        nums[0] = 1
        nums[1] = 2
        for i in range(2, n):
            nums[i] = nums[i-1] + nums[i - 2]
        return nums[-1]


# @lc code=end

