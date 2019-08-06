def avage():
    total = 0
    count =0
    aver =0
    while True:
        new_num = yield aver
        count+=1
        total +=new_num
        aver = total/count

def pre():
    while True:
        yield from avage()


c = pre()
next(c)
print(c.send(10))
print(c.send(20))
print(c.send(30))