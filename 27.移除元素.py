#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == val:
            return 0
        elif len(nums) == 1 and nums[0] != val:
            return 1
        
        # length > 1 case
        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1
# @lc code=end

