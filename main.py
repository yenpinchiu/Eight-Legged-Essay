import Two_Sum
import Three_Sum

if __name__ == '__main__':
    sol_2Sum = Two_Sum.Solution()
    sol_3Sum = Three_Sum.Solution()
    #print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    #print(sol.threeSum([0, 0, 0]))
    #print(sol.threeSum([0, 0]))
    print(sol_2Sum.twoSum([2, 7, 11, 15], 9))
    print(sol_2Sum.twoSum2([2, 7, 11, 15], 9))
    print(sol_2Sum.twoSum2([3, 2, 4], 6))
    print(sol_2Sum.twoSum2([3, 3], 6))