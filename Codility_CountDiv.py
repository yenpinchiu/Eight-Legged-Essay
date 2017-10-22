def solution(A, B, K):
    
    if A == 0:
        s = 0
    elif K > A:
        s = K
    else:
        s = A + A % K
    
    if K > B or B == 0:
        e = 0
    else:
        e = B - B % K

    if s > e:
        return 0
    else:
        return (e - s) / K + 1

