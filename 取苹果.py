'''
一个矩形区域被划分为N*M个小矩形格子，在格子(i,j)中有A[i][j]个苹果。现在从左上角的格子(1,1)出发，要求每次只能向右走一步或
向下走一步，最后到达(N,M)，每经过一个格子就把其中的苹果全部拿走。请找出能拿到最多苹果数的路线。
'''
class solution():
    def __init__(self,a):
        '''

        :param a: 矩阵，里面表示有多少个苹果
        '''
        self.a = a
        self.d=[[0 for _ in range(len(a[0]))] for _ in range(len(a))]

    def main(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                if i ==0:
                    self.d[i][j] = self.d[i][j-1] + self.a[i][j]
                if j ==0:
                    self.d[i][j] = self.d[i-1][j] + self.a[i][j]
                else:
                    self.d[i][j]=max(self.d[i-1][j],self.d[i][j-1])+self.a[i][j]

        return self.d[-1][-1]
s = solution([[6,5,3,5],[3,1,3,1],[1,1,2,3]])
print(s.main())