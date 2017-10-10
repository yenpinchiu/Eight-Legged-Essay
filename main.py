import Two_Sum
import Three_Sum
import Four_Sum

if __name__ == '__main__':
    #sol_2Sum = Two_Sum.Solution()
    #sol_3Sum = Three_Sum.Solution()
    sol_4Sum = Four_Sum.Solution()
    #print(sol_3Sum.threeSum2([-1, 0, 1, 2, -1, -4]))
    #print(sol_3Sum.threeSum2([0, 0, 0]))
    #print(sol_3Sum.threeSum2([0, 0]))
    #print(sol_3Sum.threeSum2([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    #print(sol_3Sum.threeSum2([-1,0,1,2,-1,-4]))
    #print(sol_3Sum.threeSum2([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    #print(sol_2Sum.twoSum([2, 7, 11, 15], 9))
    #print(sol_2Sum.twoSum2([2, 7, 11, 15], 9))
    #print(sol_2Sum.twoSum2([3, 2, 4], 6))
    #print(sol_2Sum.twoSum2([3, 3], 6))
    print(sol_4Sum.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(sol_4Sum.fourSum([0, 0, 0, 0], 0))