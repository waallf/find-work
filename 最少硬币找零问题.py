#硬币找零问题
class solution():
    def __init__(self,number,coin):
        '''

        :param number: 需要找零的钱
        :param coin: 拥有的零钱
        '''
        self.number = number
        self.coin = coin
        self.d = [1000000 for _ in range(number+1)]
        self.d[0]=0
    def main(self):
        for i in range(1,self.number+1):
            for j in self.coin:
                if i >=j:
                    self.d[i]= min(self.d[i],self.d[i-j]+1)
        return self.d[-1]


s = solution(5,[1,2])
print(s.main())