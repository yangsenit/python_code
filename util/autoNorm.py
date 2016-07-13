# -*- coding:utf-8 -*-
import numpy as np
data=[[1,2,100,4],[2,3,4,58],[34,23,54,12]]
dmat=np.mat(data)
def autoNorm(dmat):
    dmat=dmat*1.0
    (row,col)=dmat.shape
    min=dmat.min(0)
    max=dmat.max(0)
    ranges=max-min
    returndmat=np.zeros((row,col))
    for i in range(row):
        returndmat[i,:]=(dmat[i,:]-min)/ranges
    return returndmat
print autoNorm(dmat)