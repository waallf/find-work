# num = int(input())
# li = list(int (i) for i in input().split(" "))
def ind(arr,number):

    for idnex,i in enumerate(arr):
        if i >number:
            return max(idnex,0)
    return len(arr)
def out(tre):
    all = []
    quee = [tre]
    while quee:
        now = quee.pop(0)
        all.append(now.cur)
        if now.left:
            quee.append(now.left)
        if now.right:
            quee.append(now.right)

    return all
class node():
    def __init__(self,cur):
        self.cur = cur
        self.left = None
        self.right = None

def s(arr):
    if len(arr)==1:
        return node(arr[-1])

    index = ind(arr,arr[0])
    now = node(arr[0])
    if arr[1:index] != []:
        left = s(arr[1:index])
        now.left = left
    if arr[index:]!=[]:
        right = s(arr[index:])
        now.right = right
    return now

tree = s([8,3,1,6,4,7,10,14,13])
print(*out(tree))