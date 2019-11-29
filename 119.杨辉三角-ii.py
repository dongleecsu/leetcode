#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        row = [1, 1]
        for i in range(2, rowIndex + 1):
            next_row = [1] * (i+1)
            for j in range(1, i):
                next_row[j] = row[j] + row[j - 1]
            row = next_row
        return next_row

# @lc code=end

