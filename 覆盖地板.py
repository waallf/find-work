#题意：用 1 * 2 的瓷砖覆盖 n * m 的地板，问共有多少种覆盖方式？
#思路：用2进制，第i行纸盒i-1行有关，枚举i-1行
#的每个状态，推出由此状态能达到的i行状态，如果i-1行的某一位置为未放置，
#那么必然要在i行竖放，所以对上一行的状态按位取反之后的状态就是放置了竖
#方块的状态
class solution():
    def __init__(self,m,n):
        '''
        :param m: 行数
        :param n: 列数
        '''
        self.m= m
        self.n = n
        self.dp = [[0 for _ in range(2**n)] for _ in range(m+1)]# dp[i][j]表示第i行j的方法的总数,因为第0
        #行的状态要设置为0，所以需要行数+1  
    def dfs(self,lim,state,num,i):
        '''
        :param lim: 目前的列数
        :param state: 状态
        :param num :该状态的数量
        :param  :第i行
        :return:
        '''
        if lim == self.n:
            self.dp[i][state]+=num
            return
        self.dfs(lim+1,state,num,i)#本位置不放砖
        # lim 与lim+1位置横放一块砖
        '''
        这段代码的意思是，当state是某一状态的时候，在能够横着放砖的位置放上砖，放上砖后状态更新
        '''
        if (lim<=self.n-2 )and not(state&(2**lim)) and not(state&((2**(lim+1)))):
            state = state|(2**lim)|(2**(lim+1))
            self.dfs(lim+2,state,num,i)
    def mian(self):
        self.dfs(0,0,1,1)
        for i in range(2,self.m+1):
            for j in range(2**self.n):
                tmp =self.dp[i-1][j]#如果没有值，表示没有存放值
                if tmp:
                    self.dfs(0,(~j)&(2**self.n-1),tmp,i)
                else:
                    continue
        print(self.dp[-1][-1])#因为放置是一环套一环，所以看达到最后状态的有多少次就可以了


s = solution(4,4)
s.mian()

