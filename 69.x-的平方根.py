#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    # 二分法求解
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left, right = 0, x
        while True:
            middle = int((left + right)/2)
            if middle**2 <= x and (middle + 1)**2 > x:
                return middle
            if middle**2 < x:
                left = middle
            elif middle**2 > x:
                right = middle

sol = Solution()
x = 4
out = sol.mySqrt(x)
# @lc code=end

