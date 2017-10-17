class Solution(object):
    def isSingleSwapSorted(self, nums):
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