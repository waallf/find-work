#代价最短路径问题
'''
无向图G中有N个顶点，并通过一些边相连接，边的权值均为正数。初始时你身上有M元，当走过i点时，
需要支付S(i)元，如果支付不起表示不能通过。请找出顶点1到顶点N的最短路径。如果不存在则返回一个特殊值，
如果存在多条则返回最廉价的一条。限制条件：1<N<=100; 0<=M<=100 ; 对任意i, 0<=S[i]<=100。
'''
class solution():
    def __init__(self,s,m,n):
       '''
       :param s: 列表，值为在i节点要出的费用
       :param m: 身上的钱
       :param n: 节点个数

       '''
       self.s =s#一般情况下，s应该是个矩阵，表示i到j需要花费多少
       self.m = m
       self.n = n
       self.mat =[ ['Inf' for _ in range(len(s)) ]for _ in range(len(s))]
       self.state=[[0 for _ in range(len(s))]for _ in range(len(s))]#记录路径
       for i in range(self.n):#初始化
           self.mat[i][i]=0
           for j in range(self.n):
               if i!=j:
                self.mat[i][j]=s[i]
    def daijialujing(self):
        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    self.mat[k][j]=min(self.mat[k][j],self.mat[k][i]+self.mat[i][j])
                    self.state[k][j]=k if self.mat[k][j]<=self.mat[k][i]+self.mat[i][j] else i

        for i in range(n):
            print(self.mat[0][i])
           

s = solution([2,3,5,1,3,6,1],m=6,n=7)
print(s.daijialujing())
