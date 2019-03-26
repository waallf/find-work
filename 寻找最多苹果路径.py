def fing_max_apple(A):
    '''
    :param A:一个矩阵，A[i,j]表示有几个苹果
    :return: 1，1 到n,m 最多取得多少个苹果
    '''
    max_number = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            if i <1 and j <1:
                max_number[i][j] = A[i][j]
            elif i<1:
                max_number[i][j] =max_number[i][j - 1] + A[i][j]
            elif j<1:
                max_number[i][j] =max_number[i-1][j] + A[i][j]
            else:
                max_number[i][j] =max(max_number[i][j-1],max_number[i-1][j]) +A[i][j]
    return max_number[-1][-1]
print(fing_max_apple([[1,2,3],[1,200,3],[1,2,3]]))