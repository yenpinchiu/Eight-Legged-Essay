'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
    def twoSum(self, nums, target):
        viewd_dic = {}

        for i in range(0, len(nums)):
            partner = target - nums[i]

            if partner in viewd_dic:
                return [viewd_dic[partner], i]

            viewd_dic.update({nums[i]: i})

        return None; # exactly one solution

    def twoSum2(self, nums, target):
        
        nums_with_index = []
        for i, k in enumerate(nums):
            nums_with_index.append([k, i])

        nums_with_index.sort(key = lambda x : x[0])
        sorted_nums_with_index = nums_with_index

        head = 0
        tail = len(nums) - 1

        while head != tail:
            if sorted_nums_with_index[head][0] + sorted_nums_with_index[tail][0] == target:

                return [sorted_nums_with_index[head][1], sorted_nums_with_index[tail][1]]
            elif sorted_nums_with_index[head][0] + sorted_nums_with_index[tail][0] > target:
                tail -= 1
            elif sorted_nums_with_index[head][0] + sorted_nums_with_index[tail][0] < target:
                head += 1

        return None; # exactly one solution