'''
給定一個int list A,從A裡面切出一個sub list,此sub list所有數值的合是A的所有sub list中最大的,求此sub string所有數值的合

A = [5, -7, 3, 5, -2, 4, -1]
其中A[2] ~ A[4]的合為 3 + 5 - 2 + 4 = 10,為最大，故return 10

可以是空subarray,合為0那樣

'''

# 基本想法就,以A[i]為尾的sub array中的合最大者,要馬是A[i-1]為尾的最大者+A[i],要馬是A[i]自己,要馬就空集合(A[i]自己也是負的時)
# 不可能是"一部分"的A[i-1]為尾的最大者+A[i],因為如果是這樣,再往前延伸一定會更大,所以一定是全包
# 而其中A[i-1]為尾的最大者+A[i]的合一定>=A[i],因為不管怎樣都能空集合,所以A[i-1]為尾的最大者一定>=0
# A[i-1]為尾的最大者為空集合其實就是不該包含A[i-1]為尾的最大者的意思
def MaximunSubarray(A):
    local_max = 0
    global_max = 0

    for i in range(0, len(A)):
        # 計算停在此的sub array中合最大者的合
        # 不需要max(0, local_max + i, i),因為local_max最小值是0,所以local_max + i一定 >= i
        # 如果0贏了,表示A[i - j] + A[i - j + 1] + .... + A[i]不管j取多少都是負的,不如空集合
        # 如果local_max + A[i]贏了,且local_max = 0,表示A[i - j] + A[i - j + 1] + .... + A[i - 1]不管j取多少都是負的,而A[i]為正,所以只包含A[i]是最好的
        # 如果local_max + A[i]贏了,且local_max != 0,A[i-1]為尾的最大者+A[i]是最好的
        # A[i] = 0的情況很trival,不特別討論
        local_max = max(0, local_max + A[i]) 
        # 保留全部sub array中的最大者
        global_max = max(global_max, local_max)
    
    return global_max

if __name__ == "__main__":
    print(MaximunSubarray([5, -7, 3, 5, -2, 4, -1]))