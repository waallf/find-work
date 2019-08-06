def Len_subchar(s1):
    prefer = [-1]*26
    l=0
    r=0
    out=0
    curlength=0
    maxlength = 0
    for i in range(0,len(s1)):
        if prefer[ord(s1[i])-ord('a')]<0 or i- prefer[ord(s1[i])-ord('a')]>curlength:
            curlength+=1
        else:
            maxlength = max(maxlength,i-prefer[ord(s1[i])-ord('a')])
            curlength = i-prefer[ord(s1[i])-ord('a')]
        prefer[ord(s1[i])-ord('a')]=i
            
    maxlength = max(curlength,maxlength)
    return maxlength
print(Len_subchar('arabcafr'))

