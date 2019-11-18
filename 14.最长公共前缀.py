#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        if len(strs) == 1:
            return strs[0]
        out = ''
        for i, e in enumerate(strs[0]):
            flag = True
            for s in strs[1:]:
                if len(s) > i:
                    if s[i] != e:
                        flag = False
                        return out
                else:
                    return out
            if flag:
                out += e
        return out
# @lc code=end

