#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        else:
            return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


# @lc code=end

