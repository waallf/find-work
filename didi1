n = int(input())
li = input().split(" ")
fu = ['+',"-","*","/"]
i = 0
mow_zi = []
def paixu(zhan,c):
    zhan.sort()
    zhan = [str(i) for i in zhan]
    return (" "+c+" ").join(zhan)
now_zhan = []
ress=''
while i <len(li):
    if li[i] in fu:
        if mow_zi==[]:
            mow_zi = li[i]
            i+=1
        else:
            if li[i]!=mow_zi[0]:
                if (li[i]=="*" or li[i]=="/") and not(mow_zi[0]=="*" or mow_zi[0]=="/"):
                    res = paixu(now_zhan[:-1],mow_zi[0])
                    ress += res + " " + mow_zi[0]+ " "
                    now_zhan=[now_zhan[-1]]

                else:
                    res = paixu(now_zhan,mow_zi[0])
                    ress += res + " " + li[i] + " "
                    i+=1
                    now_zhan = []
                mow_zi=[]
                continue
            else:
                i+=1
    else:
        now_zhan.append(int(li[i]))
        i+=1

if len(now_zhan)==1:
    ress +=str(now_zhan[0])
else:
    ress += paixu(now_zhan,mow_zi[0])
print(ress)
