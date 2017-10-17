# number of visible nodes in a binary tree

class Solution(object):
    def CountVisibleNodes(self, root):
        return self.scan_nodes(root, root.x)

    def scan_nodes(self, root, max_value):
        count = 0

        if root.x >= max_value:
            max_value = root.x
            count += 1

        if root.left is not None:
            count += self.scan_nodes(root.left, max_value)

        if root.right is not None:
            count += self.scan_nodes(root.right, max_value)

        return count

class node:
    def __init__(self, x, left, right):
        self.x = x
        self.left = left
        self.right = right

if __name__ == "__main__":
    n_23 = node(1, None, None)
    n_22 = node(21, None, None)
    n_21 = node(20, None, None)
    n_12 = node(10, n_23, None)
    n_11 = node(3, n_21, n_22)
    n_0 = node(5, n_11, n_12)

    s = Solution()
    print(s.CountVisibleNodes(n_0))