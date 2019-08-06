def zuhe(s,number,result):
    if number ==0:
        print(*result)
        return
    if s=='':
        return
    result.append(s[0])
    zuhe(s[1:],number-1,result)
    result.pop(-1)
    zuhe(s[1:],number,result)

def pailie(n,start):
    if start == len(n) - 1:
        print(*n)
        return

    for i in range(start,len(n)):
        s=n[start]
        n[start]=n[start+1]
        n[start]=s
        pailie(n,start+1)
        s = n[start]
        n[start] = n[start + 1]
        n[start] = s
n='abc'
# pailie(list(n),start=0),

for i in range(1,len(n)+1):
    result=[]
    zuhe(n,i,result)

