'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        sorted_nums = sorted(nums)
        
        results = []
        nums_len = len(sorted_nums)

        for i in range(0, nums_len - 1):
          num_i = sorted_nums[i]
          if i > 0 and num_i == sorted_nums[i-1]:
                  continue

          for j in range(i + 1, nums_len - 1):
              num_j = sorted_nums[j]
              if j > i + 1 and num_j == sorted_nums[j-1]:
                  continue

              head = j + 1
              tail = nums_len - 1

              i_j_target = target - num_i - num_j

              while head < tail:
                num_head = sorted_nums[head]
                num_tail = sorted_nums[tail]
                num_head_tail_sum = num_head + num_tail

                i_j_sum = num_i + num_j
                if num_head_tail_sum == i_j_target:
                    results.append([num_i, num_j, num_head, num_tail])
                    head += 1
                    tail -= 1
                    
                    while head < tail and sorted_nums[head] == sorted_nums[head - 1]:
                        head += 1

                    while head < tail and sorted_nums[tail] == sorted_nums[tail + 1]:
                        tail -= 1

                elif num_head_tail_sum > i_j_target:
                    tail -= 1

                elif num_head_tail_sum < i_j_target:
                    head += 1

        return results