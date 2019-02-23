# -*- coding:utf-8 -*-
#易于理解版
class Solution:
    def InversePairs(self, data):
        # write code here
        copy_data = data[:]
        start = 0
        end = len(data)-1
        result = self.main(copy_data, data, start, end)
        print(result % 1000000007)

    def main(self, copy_data, data, start, end):
        if start == end:
            copy_data[start] = data[start]
            return 0
        else:
            midim = int((end - start)/2)
            left = self.main(data, copy_data, start, start+midim)
            right = self.main(data, copy_data, start+midim + 1, end)
            i = start + midim
            j = end
            count = 0
            copy_index = end
            while (i >= start and j >= start+midim+1):
                if data[i] > data[j]:
                    count = count +j-start-midim
                    copy_data[copy_index ] = data[i]
                    copy_index-=1
                    i-=1
                else:
                    copy_data[copy_index] = data[j]
                    copy_index-=1
                    j-=1
            for q in range(i,start-1,-1):
                copy_data[copy_index] = data[q]
                copy_index-=1
            for w in range(j,start+midim,-1):
                copy_data[copy_index] = data[w]
                copy_index -= 1
            return left + right + count


s=Solution()
s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575])
# python ac版
class Solution:
    def InversePairs(self, data):
        # write code here
        return self.inverseCount(data[:], 0, len(data) - 1, data[:]) % 1000000007

    def inverseCount(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start + end) // 2
        cnt = self.inverseCount(data, start, mid, tmp) + self.inverseCount(data, mid + 1, end, tmp)
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start

        while (i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while (i <= mid):
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while (j <= end):
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt
