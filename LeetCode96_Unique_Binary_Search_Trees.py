'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class Solution(object):
    recur_result_dict = {2:2, 1:1, 0:1}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.numSubTrees(n)

    def numSubTrees(self, n):
        if n in self.recur_result_dict:
            return self.recur_result_dict[n]
        
        result = 0
        for i in range(0, n):
            result += self.numSubTrees(i) * self.numSubTrees(n - i - 1)

        if n not in self.recur_result_dict:
            self.recur_result_dict.update({n:result})

        return self.recur_result_dict[n]