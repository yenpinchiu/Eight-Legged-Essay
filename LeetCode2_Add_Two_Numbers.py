'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoDigits(self, l1, l2, pre_node, add):
        if l1 is None and l2 is None and add is 0:
            return

        if pre_node is None:
            cur_node = ListNode(0)
        else:
            pre_node.next = ListNode(add)
            cur_node = pre_node.next

        if l1 is not None:
            cur_node.val += l1.val
        if l2 is not None:
            cur_node.val += l2.val
        add = int(cur_node.val / 10)
        cur_node.val = cur_node.val % 10

        self.addTwoDigits(l1.next if l1 is not None else l1, l2.next if l2 is not None else l2, cur_node, add)

        return cur_node

    def addTwoNumbers(self, l1, l2):
        start_node = self.addTwoDigits(l1, l2, None, 0)
        return start_node