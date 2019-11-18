#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    """双指针基本题型，一前一后滑动"""
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        p1, p2 = 0, len(str_x) - 1
        while p1 < p2:
            if str_x[p1] == str_x[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
        
# @lc code=end

