class Solution(object):
    def SortWithSingleSwap(self, num_list):
        sorted_num_list = sorted(num_list)
        
        diff_count = 0
        for i in range(0, len(num_list)):
            if sorted_num_list[i] != num_list[i]:
                diff_count += 1

        if diff_count > 2:
            return False

        return True

    def SortWithSingleSwap2(self, num_list):
        disorderd_index = -1

        pre_num = -1
        pre_index = -1
        for i in range(0, len(num_list)):
            if num_list[i] < pre_num:
                disorderd_index =  pre_index
            pre_num = num_list[i]
            pre_index = i
        
        return pre_num

if __name__ == "__main__":
    s = Solution()
    print(s.SortWithSingleSwap2([1, 5, 3, 3, 7]))