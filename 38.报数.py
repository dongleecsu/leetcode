#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        num = '1'
        for i in range(n - 1):
            voice = []
            v = str(num)
            cnter = 1
            str_val = ''
            e = 0
            for j, e in enumerate(v):
                if len(voice) > 0:
                    if voice[-1] == e:
                        cnter += 1
                    else:
                        str_val += str(cnter) + str(v[j-1])
                        cnter = 1
                voice.append(e)

            str_val += str(cnter) + '1'
            num = str_val
        return num



        
# @lc code=end

