class Matrix_Chain():
    def __init__(self,quen):
        self.s = [['Inf']*len(quen)]*len(quen)
        self.m = [['Inf']*len(quen)]*len(quen)
        for i in range(len(quen)):
                    self.m[i][i] = 0
    def mul_(self,p,i,j):
        '''
        :param m: m[i][j]表示ai-aj最少乘的次数
        :param p: p[i-1]表示ai的第一维度，
        :param i:
        :param j:
        :return:
        '''
        if self.m[i][j]<'Inf':
            return self.m[i][j]

        else:
            for k in range(i,j):#在i,j之间找一个合适的切分点
                q = self.mul_(p,i,k)+self.mul_(p,k+1,j)+p[i-1]*p[k]*p[j]
                if q<self.m[i][j]:
                    self.m[i][j]=q
                    self.s[i][j]=k
        return self.m,self.s
    def print_result(self,i,j):
        if i==j:
            print('A'+str(i))
        else:
            print("(")
            self.print_result(i,self.s[i][j])
            self.print_result(self.s[i][j]+1,j)
            print(")")


