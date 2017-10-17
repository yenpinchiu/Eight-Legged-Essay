class Solution(object):
    def isSingleSwapSorted(self, num_list):
        sorted_num_list = sorted(num_list)
        
        diff_count = 0
        for i in range(0, len(num_list)):
            if sorted_num_list[i] != num_list[i]:
                diff_count += 1

        if diff_count > 2:
            return False

        return True

    def isSingleSwapSorted2(self, nums):
        for i in range(0, len(nums)):
            if i + 1 < len(nums) and nums[i + 1] < nums[i]:
                for j in range(i + 1, len(nums)):
                    if nums[i] > nums[j]:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp

        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.isSingleSwapSorted([1, 5, 3, 3, 7]))
    print(s.isSingleSwapSorted([1, 9, 3, 4, 7, 2]))
    print(s.isSingleSwapSorted([1, 9, 3, 5, 4, 7, 2]))