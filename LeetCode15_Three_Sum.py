'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        wait_dict = {}
        result_list = []
        duplicate_list = set()

        for i in range(0, len(nums)):
            if nums[i] in wait_dict:
                for waiting_pair in wait_dict[nums[i]]:
                    if i > waiting_pair[0][1] and i > waiting_pair[1][1]:

                        sorted_triple = sorted([waiting_pair[0][0], waiting_pair[1][0], nums[i]])
                        if str(sorted_triple) not in duplicate_list:
                            result_list.append(sorted_triple)
                            duplicate_list.add(str(sorted_triple))

            for j in range(i+1, len(nums)):

                num_k = -(nums[i] + nums[j])

                if num_k not in wait_dict:
                    wait_dict.update({num_k : []})
                
                wait_dict[num_k].append([[nums[i], i], [nums[j], j]])

        return result_list

    def threeSum2(self, nums):
        sorted_nums = sorted(nums)
        
        results = []
        nums_len = len(sorted_nums)

        for i in range(0, nums_len - 1):

            num_i = sorted_nums[i]
            if i > 0 and num_i == sorted_nums[i-1]:
                continue

            head = i + 1
            tail = nums_len - 1
            while head < tail:
                num_head = sorted_nums[head]
                num_tail = sorted_nums[tail]
                num_head_tail_sum = num_head + num_tail

                if num_head_tail_sum == - num_i:
                    results.append([num_i, num_head, num_tail])
                    head += 1
                    tail -= 1
                    
                    while head < tail and sorted_nums[head] == sorted_nums[head - 1]:
                        head += 1

                    while head < tail and sorted_nums[tail] == sorted_nums[tail + 1]:
                        tail -= 1

                elif num_head_tail_sum > - num_i:
                    tail -= 1
 
                elif num_head_tail_sum < - num_i:
                    head += 1

        return results