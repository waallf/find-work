# 输出第几个丑数
def C_s(n):
    m2 = 0
    m3 = 0
    m5 = 0

    a = [1]
    for i in range(1,n):
        m_in = min(a[m2]*2,a[m3]*3,a[m5]*5)
        a.append(m_in)
        while a[m2]*2 <= a[i]:
            m2+=1
        while a[m3]*3 <= a[i]:
            m3+=1
        while a[m5]*5 <= a[i]:
            m5+=1
    return a[-1]
print(C_s(4))