#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
        special_mapping = {'IV': 4, 'IX': 9,
                           'XL': 40, 'XC': 90,
                           'CD': 400, 'CM': 900}
        if s in special_mapping:
            return special_mapping[s]
        
        val = 0
        for k in special_mapping.keys():
            if k in s:
                val += special_mapping[k]
                s = s.replace(k, '')
        for e in s:
            val += mapping[e]
        return val

# @lc code=end

