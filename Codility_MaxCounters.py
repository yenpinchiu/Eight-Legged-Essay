def solution(N, A):
    counters = [0] * N
    max_counter = 0
    max_counter_set = max_counter
    for inst in A:
        if inst <= N:
            if counters[inst - 1] >= max_counter_set:
                counters[inst - 1] += 1
            else:
                counters[inst - 1] = max_counter_set + 1
                
            if counters[inst - 1] > max_counter:
                max_counter = counters[inst - 1]
        else:
            max_counter_set = max_counter

    for i in range(0, len(counters)):
        if counters[i] < max_counter_set:
            counters[i] = max_counter_set
            
    return counters

