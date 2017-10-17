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
        already_sort = False

        for i in range(0, len(nums)):
            if i + 1 < len(nums) and nums[i + 1] < nums[i]:
                if already_sort is True:
                    return False

                for j in range(len(nums) - 1, i, -1):
                    if nums[i] > nums[j]:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
                        already_sort = True
                
                if already_sort is False:
                    return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isSingleSwapSorted([1, 5, 3, 3, 7]))
    print(s.isSingleSwapSorted([1, 5, 3, 7]))
    print(s.isSingleSwapSorted([1, 9, 3, 4, 7, 2]))
    print(s.isSingleSwapSorted([1, 9, 3, 5, 4, 7, 2]))
    print(s.isSingleSwapSorted([]))
    print(s.isSingleSwapSorted([1, 1, 1, 1, 0]))
    print(s.isSingleSwapSorted([1, 6, 5, 2]))
    print("---------------------------")
    print(s.isSingleSwapSorted2([1, 5, 3, 3, 7]))
    print(s.isSingleSwapSorted2([1, 5, 3, 7]))
    print(s.isSingleSwapSorted2([1, 9, 3, 4, 7, 2]))
    print(s.isSingleSwapSorted2([1, 9, 3, 5, 4, 7, 2]))
    print(s.isSingleSwapSorted2([]))
    print(s.isSingleSwapSorted2([1, 1, 1, 1, 0]))
    print(s.isSingleSwapSorted2([1, 6, 5, 2]))