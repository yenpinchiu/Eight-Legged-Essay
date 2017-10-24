def solution(A):
    border_index_dict = {}
    border_index_list = []
    
    for i in range(0, len(A)):
        if i - A[i] not in border_index_dict:
            border_index_dict.update({i - A[i] : []})
            border_index_list.append(i - A[i])
        border_index_dict[i - A[i]].append(i)
        
        if i + A[i] not in border_index_dict:
            border_index_dict.update({i + A[i] : []})
            border_index_list.append(i + A[i])
        border_index_dict[i + A[i]].append(i)

    result = 0
    indiscs = set()
    for i in sorted(border_index_list):
        remove_set = set()
        for discs in border_index_dict[i]:
            if discs not in indiscs:
                result += len(indiscs)
                indiscs.add(discs)
            else:
                remove_set.add(discs)
        
        for discs in remove_set:
            indiscs.remove(discs)
            
    if result > 10000000:
        return -1
    else:
        return result

