def solution(S, P, Q):
    nuc_prefix_his = []
    for i in range(0, len(S)):
        if i - 1 >= 0:
            nuc_prefix_his.append(list(nuc_prefix_his[i - 1]))
        else:
            nuc_prefix_his.append([0, 0, 0, 0])
        
        if S[i] == 'A':
            nuc_prefix_his[i][0] += 1
        elif S[i] == 'C':
            nuc_prefix_his[i][1] += 1
        elif S[i] == 'G':
            nuc_prefix_his[i][2] += 1
        elif S[i] == 'T':
            nuc_prefix_his[i][3] += 1
    
    result = []
    for i in range(0, len(P)):
        if P[i] != 0:
            before_his = nuc_prefix_his[P[i] - 1]
        else:
            before_his = [0, 0, 0, 0]
        
        after_his = nuc_prefix_his[Q[i]]
        
        for j in range(0, 4):
            if after_his[j] - before_his[j] > 0:
                result.append(j + 1)
                break
        
    return result