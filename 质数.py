m1 = 2
m3 =3
m5=5
m7 =7
m = min(m1*2,m3*2,m5*2,m7*2 )
n = 100
while m<n:

    i=2
    while m1<m:
        m1 *= i
        i+=1
    i = 2
    while m3< m:
        m3 *= i
        i += 1
    i = 2
    while m5< m:
        m5 *= i
        i += 1
    i = 2
    while m7< m:
        m7 *= i
        i += 1
    m = min(m1, m3, m5, m7)

if m>=n:
    print('Yes')