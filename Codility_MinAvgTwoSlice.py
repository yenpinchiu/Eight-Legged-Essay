
def solution(A):
    init_flag = False
    min_avg = 0
    min_index = 0
    
    for i in range(0, len(A)):
        has_cur_avg = False
        if i + 2 < len(A):
            len_3_slice_avg = float(A[i] + A[i + 1] + A[i+2]) / 3
            len_2_slice_avg = float(A[i] + A[i + 1]) / 2
            
            if len_2_slice_avg <= len_3_slice_avg:
                cur_min_avg = len_2_slice_avg
            else:
                cur_min_avg = len_3_slice_avg  
            has_cur_avg = True
        elif i + 1 < len(A):
            cur_min_avg = float(A[i] + A[i + 1]) / 2
            has_cur_avg = True

        if (init_flag is False or cur_min_avg < min_avg) and has_cur_avg:
            min_avg = cur_min_avg
            min_index = i
            init_flag = True
    
    return min_index

