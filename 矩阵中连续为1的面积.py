b =[[1,0,0],[1,1,0],[1,0,1]]
n = len(b)
visted = [[0 for _ in range(n)] for _ in range(n)]
def find_num(i,j):
    if  i<0 or i>=n or j<0 or j>=n or visted[i][j]!=0 or b[i][j]==0:
        return 0
    else:
        visted[i][j]=1
        return 1+find_num(i,j+1) +find_num(i+1,j)+find_num(i-1,j)+find_num(i,j-1)
p_list = 0
for i in range(n):
    for j in range(n):
        if b[i][j]==1 and visted[i][j]==0:
            p_list =max(p_list,find_num(i,j))
print(p_list)