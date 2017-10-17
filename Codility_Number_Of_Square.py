# number of whole square number within a range

import math

class Solution(object):
    def FindSquareNumNum(self, a, b):
        min_squre_num = math.ceil(math.sqrt(a))
        max_squre_num = math.floor(math.sqrt(b))

        return max_squre_num - min_squre_num + 1

if __name__ == "__main__":
    s = Solution()
    print(s.FindSquareNumNum(4, 17))