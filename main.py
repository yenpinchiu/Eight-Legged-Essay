import Remove_Nth_Node_From_End_of_List as remove_node

if __name__ == '__main__':
    n5 = remove_node.ListNode(5, None)
    n4 = remove_node.ListNode(4, n5)
    n3 = remove_node.ListNode(3, n4)
    n2 = remove_node.ListNode(2, n3)
    n1 = remove_node.ListNode(1, n2)
    head = n1

    s = remove_node.Solution()
    head = s.removeNthFromEnd(head, 2)
    print(s.printList(head))

