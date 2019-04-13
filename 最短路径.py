num = int(input())
ns = []
ms=[]
vals= []
costs=[]
for  i in range(num):
    n,m = [int(o) for o in input().split(" ")]
    val = [int(o) for o in input().split(" ")]
    cost  = [[999999999 for _ in range(n)] for _ in range(n)]
    for j in range(m):
        a,b,c = [int(h) for h in input().split(" ")]
        cost[a-1][b-1] = c
        cost[b-1][a-1] = c
    for t in range(n):
        cost[t][t]=0

    ns.append(n)
    ms.append(m)
    vals.append(val)
    costs.append(cost)
def aa(n,m,val,cost):
    midss=[]
    for index,pp in enumerate(val):
        st_val = pp
        st = index
        lu = [st]
        have_v = [st]
        mids = []
        for q in range(n-1):
            infine = 9999999999
            for p in range(n):
                if infine>cost[st][p] and p not in have_v:
                    infine = cost[st][p]
                    mind = cost[st][p]
                    min_s = p
            mids.append(mind)
            have_v.append(min_s)
            for l  in range(n):
                if mind + cost[min_s][l] <cost[st][l]:
                    cost[st][l]=mind + cost[min_s][l]
        midss.append(sum(mids))
    print(min(midss))
for n,m,val,cost in zip(ns,ms,vals,costs):
    aa(n,m,val,cost)







