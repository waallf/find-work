def dizeng_subquene(queue):
    lit = [1] * len(queue)
    for index,i in enumerate(queue):
        for jndex,j in enumerate(queue[:index]):
            if i>j and lit[jndex]+1>lit[index]:
                lit[index]=lit[jndex]+1
    return max(lit)
print(dizeng_subquene([3,1,4,1,5,9,2,6,5]))
