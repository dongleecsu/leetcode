#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    """
    目标是*遍历一遍数组*
    因此采用哈希表，key为差值，则后续遍历时若在字典中找到了
    key，则可直接返回。
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i

        # for i in range(len(nums) - 1):
        #     val = target - nums[i]
        #     if val in nums[i+1:]:
        #         j = nums[i+1:].index(val) + i + 1
        #         return [i, j]

            # for j in range(i + 1, len(nums)):
            #     if nums[i] + nums[j] == target:
            #         return [i, j]
# @lc code=end

