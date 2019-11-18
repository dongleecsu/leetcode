#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (33.20%)
# Likes:    1466
# Dislikes: 0
# Total Accepted:    221.1K
# Total Submissions: 665.9K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        BOUND = 2**31
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1
        else:
            return 0
        
        nums = []
        x = abs(x)
        while x // 10 > 0:
            nums.append(x % 10)
            x = x // 10
        if x > 0:
            nums.append(x % 10)
        if sign > 0:
            val = 0
            for e in nums:
                if e == 0 and val == 0:
                    continue
                val = val * 10 + e
                if val > BOUND - 1:
                    return 0
            return val
        else:
            val = 0
            for e in nums:
                if e == 0 and val == 0:
                    continue
                val = val * 10 + e
                if val > BOUND:
                    return 0
            return -1*val
        
        
# @lc code=end

