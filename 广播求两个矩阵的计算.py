import numpy as np
def F(A,B):
    if A.shape[1]!=B.shape[1]:
        return 0
    C = np.zeros((A.shape[0],B.shape[0]))
    for i in range(A.shape[0]):
        exA= np.expand_dims(A[i],0)
        C[i]= np.sum((exA-B)**2,axis=1)
    return C
print(F(np.ones((3,3)),np.ones((4,3))))
