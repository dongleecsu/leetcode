#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root and root.val == sum:
            if not (root.left or root.right):
                return True
        if root.left and root.right:
            return self.hasPathSum(root.left, sum - root.val) or \
                    self.hasPathSum(root.right, sum - root.val)
        if root.left:
            return self.hasPathSum(root.left, sum - root.val)
        if root.right:
            return self.hasPathSum(root.right, sum - root.val)
        return False
        
# @lc code=end

