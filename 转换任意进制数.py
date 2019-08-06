def C2k(number,K):
    out = []
    if number==0:
        return 0
    while number!=0:
        out.append(str(number%K))
        number = (number - int(out[-1]))//K
    out.reverse()
    out = "".join(out)
    return out
'''
测试：
1462254977029824 5
输出：
3013130041143104423244
'''
# number,K = list(int(i) for i in input().split(" "))
number=1462254977029824
K = 5
print(C2k(number,K))
