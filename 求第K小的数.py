def Parition(data):
    need = data[-1]
    small =0
    big = len(data)-1
    while small<big:
        while small<big and data[small]<=need:
            small+=1
        data[big] = data[small]
        while small<big and  data[big]>=need:
            big-=1
        data[small] = data[big]
    data[small]=need
    return  data,small
def main(data,k):
    k= k-1#对其下标
    data,re_k = Parition(data)
    while re_k!=k:
        if re_k<k:
            data, re_k=Parition(data[re_k:])
        else:
            data, re_k =Parition(data[:re_k])
    return data[k]

print(main([3,4,2,1,6],2))