import functools

a = ['1','2','3']
def pai(s1,s2):
    if s1+s2< s2+s1:
        return -1
    else:
        return 1


b = sorted(a,key=functools.cmp_to_key(pai))
print(b)