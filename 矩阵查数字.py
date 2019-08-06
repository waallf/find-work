'''
给定一个二维整型矩阵，已知矩阵的每一行都按照从小到大的顺序排列，每一列也都按照从小到大的顺序排列。现在给出一个数，请写一个函数返回该数是否存在于矩阵中。
矩阵中出现的数字与需要查找的数(k)都为0~100000之间的整数，且矩阵的大小在3000*3000以内。
在保证正确性的基础上，请尽量给出比较高效的解法。请列出你的算法时间复杂度与空间复杂度分别是多少
'''
m,n = list(int(i) for i in input().split(" "))
mat = list(0 for _ in range(n))
for i in range(m):
    mat[i] = list(int(i) for i in input().split(" "))
number = int(input())

i = 0#行数
j = n-1#列数
while i<len(mat) and j >=0 and mat[i][j]!=number:
    if mat[i][j]<number:
        i+=1
    else:
        j-=1
if i>=m or j <0:
    print('false')
else:
    print('true')
