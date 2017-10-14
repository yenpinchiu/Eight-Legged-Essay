'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass. 
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x, next_node):
         self.val = x
         self.next = next_node

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur_node = head
        index = 1
        node_dict = {index:head}
        
        while cur_node.next != None:
            cur_node = cur_node.next
            index += 1
            node_dict.update({index:cur_node})

        if index - n + 2 not in node_dict:
            r_node = None
        else:
            r_node = node_dict[index - n + 2]

        if index - n in node_dict:
            l_node = node_dict[index - n]
        else:
            l_node = None

        if r_node is not None and l_node is not None:
            l_node.next = r_node
            return head
        elif r_node is not None and l_node is None:
            return r_node
        elif r_node is None and l_node is not None:
            l_node.next = None
            return head
        else:
            return None

    def printList(self, head):
        cur_node = head
        result = ""
        while cur_node != None:
            result += str(cur_node.val) + " -> "
            cur_node = cur_node.next

        return result