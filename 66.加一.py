#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] < 10:
            return digits

        done = False
        i = len(digits) - 1
        while i >= 0:
            if i == len(digits) - 1:
                digits[i] = 0
                i -= 1
                continue
            if digits[i] < 9:
                digits[i] += 1
                done = True
                break
            else:
                digits[i] = 0
            i -= 1
        
        if not done:
            digits = [1] + [0] * len(digits)
        return digits

        
# @lc code=end

