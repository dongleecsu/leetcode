#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if needle not in haystack:
            return -1
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i + len(needle)] == needle:
                    return i
        return -1
            
# @lc code=end

