def solution(A):
    his_backward = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        if i + 1 <= len(A) - 1:
            his_backward[i] = his_backward[i + 1]
            
        if A[i] == 1:
            his_backward[i] += 1

    result = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            result += his_backward[i]
        if result > 1000000000:
            return -1

    return result

def solution2(A):
    result = 0
    forward_count = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            forward_count += 1

        elif A[i] == 1:
            result += forward_count

        if result > 1000000000:
            return -1

    return result

