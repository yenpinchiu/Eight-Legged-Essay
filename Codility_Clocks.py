def solution(A, P):
    clock_dict = {}
    pair_list = []

    if A is None:
        return 0

    for ci in xrange(0, len(A)):
        handIntervals = handIntervalList(sorted(A[ci]), P)
        handIntervalsStr = str(handIntervals)
        if handIntervalsStr in clock_dict:
            for ci2 in clock_dict[handIntervalsStr]:
                pair_list.append([ci2, ci])
        
            clock_dict[handIntervalsStr].add(ci)
        else:
            clock_dict.update({handIntervalsStr:set()})
            same_clock_set = clock_dict[handIntervalsStr]
            same_clock_set.add(ci)
            for ri in xrange(0, len(A[0])):
                handIntervalsRotated = handIntervals[ri:len(handIntervals)]
                handIntervalsRotated.extend(handIntervals[0:ri])
                handIntervalsRotatedStr = str(handIntervalsRotated)
                if handIntervalsRotatedStr not in clock_dict:
                    clock_dict.update({handIntervalsRotatedStr:same_clock_set})

    return len(pair_list)
            
def handIntervalList(Aci, P):
    intervalList = []
    for hi in xrange(0, len(Aci)):
        if hi + 1 >= len(Aci):
            intervalList.append(P - Aci[hi] + Aci[0] )
        else:
            intervalList.append(Aci[hi + 1] - Aci[hi])
    
    return intervalList

if __name__ == '__main__':
    clocks = [[1, 2], [2, 4], [4, 3], [2, 3], [1, 3]]
    print(solution(clocks, 4))