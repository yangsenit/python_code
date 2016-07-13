import numpy as np
dataMat=np.mat([[1,1],[8,8]])
labelMat=np.mat([[2,3]]).T
print dataMat
print "**************"
print labelMat
print np.multiply(dataMat,labelMat)
'''
2  1,1   2,2
3  8,8   24,24
'''
thetas=np.ones(2).T
print np.multiply(dataMat[1],thetas)-labelMat[1]