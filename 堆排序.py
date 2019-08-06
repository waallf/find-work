def Create(data,start):
    while start <len(data)//2+1:
        if start*2+1 >len(data) or data[start*2-1]<data[start*2]:
            # 堆排序中的计算方法从下标为1来计算的，但是这里是从0开始的，
            # 所以可以得到的位置要减1，可以达到的位置是len(data)
            min_index = start*2
        else:
            min_index = start*2+1
        if data[start-1]<=data[min_index-1]:
            break
        else:
            tmp = data[start-1]
            data[start-1] = data[min_index-1]
            data[min_index-1] = tmp
        start = min_index
    return  data
def mian(data):
    out=[]
    for i in range(len(data)//2,0,-1):
        data = Create(data,i)
    while len(data)!=1:
        out.append(data[0])
        data[0] = data[-1]
        data = Create(data[:-1],1)
    out.append(data[-1])
    print(*out)

mian([4,3,5,6,1])



