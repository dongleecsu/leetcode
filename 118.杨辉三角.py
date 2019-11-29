#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        out = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = out[-1][j-1] + out[-1][j]
            out.append(row)
        return out

sol = Solution()
outs = sol.generate(5)

# @lc code=end

