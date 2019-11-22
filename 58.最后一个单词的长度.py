#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if set(s) == ' ':
            return 0
        p = len(s) - 1
        cnter = 0
        while p >= 0:
            if s[p] != ' ':
                cnter += 1
            if cnter > 0 and s[p] == ' ':
                break
            p -= 1
        return cnter

# @lc code=end

