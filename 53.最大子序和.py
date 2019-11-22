#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """主要思路是，过去片段历史元素累计和是否为负"""
        if len(nums) == 1:
            return nums[0]

        local_sum = nums[0]
        global_sum = nums[0]
        for e in nums[1:]:
            local_sum = max(e, local_sum + e)
            global_sum = max(local_sum, global_sum)
        return global_sum

# @lc code=end

