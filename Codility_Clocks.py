class Solution(object):
    def numOfPairs(self, clocks, n, m, p):
        for clock in clocks:
            handIntervalList = self.handIntervalList(clock)
            print(handIntervalList)

        return 0
    
    def handIntervalList(self, clock):
        intervalList = []
        for hand_index in range(0, len(clock)):
            if hand_index + 1 >= len(clock):
                next_hand_index = 0
            else:
                next_hand_index = hand_index + 1

            intervalList.append(clock[next_hand_index] - clock[hand_index])
        
        return intervalList

if __name__ == '__main__':
    clocks = [[1, 2], [2, 4], [4, 3], [2, 3], [1, 3]]

    s = Solution()
    print(s.numOfPairs(clocks, 5, 2, 4))