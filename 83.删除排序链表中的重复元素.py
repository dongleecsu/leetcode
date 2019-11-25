#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = head
        if not p1:
            return head
        if p1.next:
            p2 = p1.next
        else:
            return head

        while True:
            if p1.val == p2.val:
                p2 = p2.next
                if p2:
                    continue
                else:
                    p1.next = None
                    break
            p1.next = p2
            p1 = p2
            if p2.next:
                p2 = p2.next
            else:
                break
        return head

# @lc code=end

