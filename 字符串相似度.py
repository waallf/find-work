'''
对于序列S和T，它们之间距离定义为：对二者其一进行几次以下的操作(1)删去一个字符；(2)插入一个字符；(3)改变一个字符。
每进行一次操作，计数增加1。将S和T变为同一个字符串的最小计数即为它们的距离。给出相应算法。
'''
'''
思想：
if s[-1]==t[-1]:比较前一项
else：
    修改s或t使两者最后一位而相等,dis[i][j]=dis[i-1][j-1]+1
    对s插入一个值，或t删除一个值 dis[i][j]=dis[i-1][j]+1
    相反dis[i][j]=dis[i][j-1]+1
'''
class solution():
    def __init__(self,s,t):
        self.s =s
        self.t = t
        self.dis = [[9999 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    def main(self):
        for i in range(len(self.s)+1):
            self.dis[i][0]=i
        for i in range(len(self.t)+1):
            self.dis[0][i]=i
        for i in range(1,len(self.s)+1):
            for j in range(1,len(self.t)+1):
                #self.s[i-1]是因为，self.dis存放的是从1开始的，所以要减去1才能对应上
                self.dis[i][j]= min(self.dis[i-1][j-1]+(self.s[i-1]!=self.t[j-1]),self.dis[i-1][j]+1,self.dis[i][j-1]+1)

        return self.dis[-1][-1]
s= solution(['s','s'],['b','b'])
print(s.main())