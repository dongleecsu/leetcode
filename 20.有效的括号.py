#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        mapping_dict = {'(': ')', '{': '}', '[': ']'}
        checking_list = []
        for e in s:
            if e in mapping_dict:
                # left side
                checking_list.append(e)
            else:
                # right side
                if len(checking_list) > 0:
                    if e == mapping_dict[checking_list[-1]]:
                        checking_list.pop()
                    else:
                        return False
                else:
                    return False
        if len(checking_list) == 0:
            return True
        else:
            return False

# @lc code=end

