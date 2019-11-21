#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        p = 0
        while p < len(nums):
            if nums[p] >= target:
                return p
            p += 1

# @lc code=end

