#0-1背包问题
class solution():
    def __init__(self,total,v,w):
        '''
        :param total:包的容量
        :param v: 每件物体的价值
        :param w: 每件物体的容量
        '''
        self.total = total
        self.v = v
        self.w = w
        self.m = [[0]*(total+1)]*(len(v)+1)
    def beibao(self):
        for i,v_ in enumerate(self.v):
            for j in range(1,self.total+1):
                if self.w[i]>j:
                    if i>0:
                        self.m[i][j]=self.m[i-1][j]
                    else:
                        self.m[i][j]=0
                else:
                    r1 = self.m[i-1][j-self.w[i]]+v_
                    r2 = self.m[i-1][j]
                    self.m[i][j]=max(r1,r2)
        return self.m[-1][-1]
s =solution(120,[10,25,40,20,10],[40,50,70,40,20])
print(s.beibao())




