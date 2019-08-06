def D_c(s):
    # dp[i][j]表示i-j 的字符串中的最长对称长度，对角线的位置全为1，下半区没有值
    dp =[ [[0 for _ in range(2) ]for _  in s] for _ in s]
    for i in range(len(s)):#对角线位置的值都为1
        dp[i][i][0]=1
        dp[i][i][1]=i
        if i+1 <len(s) :
            if s[i]==s[i+1]:
                # 次对角线，如果两个值相等，那么长度为2
                dp[i][i+1][0]=2
                dp[i][i+1][1]=i
            else:
                dp[i][i + 1][0] = 1
                dp[i][i + 1][1] = i+1

    for i in range(len(s)-3,-1,-1):
        for j in range(i+1,len(s)):
            if dp[i+1][j]>=dp[i][j-1]:
                dp[i][i + 1][1]=i+1
            else:
                dp[i][i + 1][1] = i
            dp[i][j]=max(dp[i+1][j],dp[i][j-1])
            if s[i]==s[j]:
                dp[i][i + 1][1] = i
                dp[i][j][0] = max( dp[i][j][0],dp[i+1][j-1][0]+2 )
    length = dp[0][-1][0]
    st = dp[0][-1][1]
    return s[st:st+length]
print(D_c('abbaad'))
