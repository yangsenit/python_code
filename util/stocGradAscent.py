# -*- coding:utf-8 -*-
'''
最原始版的随机梯度下降算法，这里书写的不是批量梯度下降算法

h=t0*1+t1*x1+t2*x2+...+tn*xn
1,f1,f2,f3 ... fn,label
'''
import numpy as np
dataMat=np.mat([[1,2,1],[1,8,8],[1,3,6]])*1.0
labelMat=np.mat([[1,1,0]]).T*1.0
print dataMat
print labelMat
import numpy as np
def stocGradAscent(dataMat,labelMat,numIter):
    m,n =dataMat.shape
    weight=np.mat(np.ones(n))*1.0
    print weight
    for j in range(numIter):
        for i in range(m):
            weight=weight- 0.01*(np.sum(np.multiply(dataMat[i], weight)) - labelMat[i, 0])*dataMat[i]
    return weight
weight= stocGradAscent(dataMat,labelMat,20)
print weight
print weight[0,1]/weight[0,2]
# print dataMat[1]
# print type(dataMat)
# print type(dataMat[1])
# print type(dataMat[1,:])
# print type(dataMat[:,1])
# m, n = dataMat.shape
# thetas = np.ones(n)
# for i in range(n):
#     thetas = thetas - 0.1 * (np.multiply(dataMat[i], thetas) - labelMat[i]) * dataMat[i]
#     print thetas
# print (np.multiply(dataMat[1], thetas) - labelMat[1])