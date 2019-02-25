#解法一：
def dizeng(queue):#返回长度
    li = [1]*len(queue)
    for index,i in enumerate(queue):
        for j in queue[:index]:
            if i>j and li[j]+1>li[i]:
                li[i]=li[j]+1
    return max(li)
#解法二
class solution():
    def __init__(self,queue):
        self.queue = queue
        self.result =[]
    def zheban(self,i,queue,start,end):
        while end >start:
            dim = (end-start)//2
            if queue[dim]>=i:
                end = dim
            else:
                start = dim+1
        return start
    def main(self):
        for idnex,i in enumerate(self.queue):
            if idnex==0:
                self.result.append(i)
            else:
                if i >self.result[-1]:
                    self.result.append(i)
                else:
                    c = self.zheban(i,self.result,0,len(self.result))
                    self.result[c]=i
        return len(self.result)

s = solution([1,-1,2,-3,4,-5,6,-7])
print(s.main())