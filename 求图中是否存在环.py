n,m = list(int(i) for i in input().split(" "))
dic = {}
'''
5 6
1 2
2 3
3 4
4 1
4 5
5 2
Yes
'''
for i in range(m):
    key,value =  list(int(i) for i in input().split(" "))
    if key in list(dic.keys()):
        dic[key].append(value)
    else:
        dic[key] = [value]
        du_key = key

def Graph_Deep(dic,du_ikey):
    #du_index 表示度为1的key值
    # 将度为1的点删除，
    while len(dic[du_ikey])==1:
        dic[du_ikey]=[]
        for key,value in dic.items():
            if du_ikey in value:
                value.remove(du_ikey)
                if len(value)==0:
                    continue
                if len(value)==1:
                    du_ikey = key
                    break
    bad =0
    for key, value in dic.items():
        if len(value)!=0:
            bad+=1
    if bad%2==0:
        return 'Yes'
    else:
        return 'No'

print(Graph_Deep(dic,du_key))