'''
题目：
假设书架上一共有9本书，每本书各有一定的页数，分配3个人来进行阅读。为了便于管理，分配时，
各书要求保持连续，比如第1、2、3本书分配给第1人，4、5分配给第二人，6，7，8，9分配给第3人，
但不能1，4，2分配给第1人，3，5，6分配给第2人。即用两个隔板插入8个空隙中将9本书分成3部分，
书不能换位。同时，分配时必须整本分配，同一本书不能拆成两部分分给两个人。为了公平起见，
需要将工作量最大的那一部分最小化，请设计分配方案。用s1,...,sn表示各本书的页数。
'''
class solution():
    def __init__(self,s,n,k):
        '''
        :param s:s[i]表示第i 本书的页数
        :param n: n本书
        :param k: 分给k个人
        '''
        self.s = s
        self.n=n
        self.k = k
        #d[i][j]表示i本书分给j个人的最小化j份中的最大值
        self.d=[[0 for _ in range(k+1)] for _ in range(n+1)]
        #flag[i][j]表示i本书，j个人，时将其分给了第j个人后还剩几本书
        self.flag = [[0 for _ in range(k+1)] for _ in range(n+1)]
        self.p=[0]*(n+1)
    def divide(self):
        for i in range(1,self.n+1):
            self.p[i]=self.p[i-1]+self.s[i-1]#累加值
            self.d[i][1]=self.p[i]#将i本书分给1个人，这个人的工作量为累加值
        for i in range(1,self.k+1):
            self.d[1][i]=self.s[0]#将1本书分给i个人，每个人的工作量时第一本书
        for i in range(2,self.n+1):
            for j in range(2,self.k+1):
                self.d[i][j]=999
                for x in range(1,i):
                    fen = max(self.d[x][j-1],self.p[i]-self.p[x])
                    if self.d[i][j]>fen:
                        self.d[i][j]=fen
                        self.flag[i][j]=x
        self.print_result(self.n,self.k)
    def print_result(self,num_book,k):
        #k表示分给k个人
        if k==1:
            for i in range(1,num_book+1):
                print(self.s[i-1])
            print("a")
        else:
            self.print_result(self.flag[num_book][k],k-1)
            for i in range(self.flag[num_book][k]+1,num_book+1):#从剩余书+1本开始输出，直到本次的num_book
                print(self.s[i - 1])
            print("a")


s = solution([1,1,1,1,1,1,1,1,1],9,3)
s.divide()

