m= list(int(i) for i in input().split(" "))
def dizeng(queue):#返回长度
    li = [1]*len(queue)
    for index,i in enumerate(queue):
        for j in queue[:index]:
            if i>j and li[j]+1>li[i]:
                li[i]=li[j]+1
    return max(li)
print(dizeng(m))
`