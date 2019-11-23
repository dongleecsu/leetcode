#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        go_up_val = 0
        out = ''
        for a_i, b_i in zip(reversed(a), reversed(b)):
            val = int(a_i) + int(b_i) + go_up_val
            go_up_val = val // 2
            val = val % 2
            out += str(val)
        if len(a) > len(b):
            for a_i in reversed(a[:-len(b)]):
                val = int(a_i) + go_up_val
                go_up_val = val // 2
                val = val % 2
                out += str(val)
        elif len(a) < len(b):
            for b_i in reversed(b[:-len(a)]):
                val = int(b_i) + go_up_val
                go_up_val = val // 2
                val = val % 2
                out += str(val)
        if go_up_val > 0:
            out += '1'
        out = out[::-1]
        return out

sol = Solution()
a_in = '1010'
b_in = '1011'
out = sol.addBinary(a_in, b_in)
# @lc code=end

