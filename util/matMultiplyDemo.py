# -*- coding:utf-8 -*-
import numpy as np
a=[[1,2],[3,4]]
b=[[0,1],[1,0]]
c=[0,0]
amat=np.mat(a)
bmat=np.mat(b)
carr=np.array([[0,1],[1,0]])
print a
print b
print amat
print bmat
print carr
print amat*carr   # mat * arr =mat  同样的是矩阵之间的乘法
print amat*bmat   # 两个矩阵就这样乘，就是矩阵之间的乘法
print c*amat
print type(c*amat)  #可以简单的得出一个结论，如果 一个不是一个数，如list np.array，这样的数据结构和矩阵相乘得到的都是矩阵
'''
#可以简单的得出一个结论，如果 一个不是一个数，如list np.array，这样的数据结构和矩阵相乘得到的都是矩阵，如果想实现点乘，
可以使用这样的方法，multipl（mat1,mat2） 两个矩阵对应对应的元素相乘
[[1, 2], [3, 4]]
[[0, 1], [1, 0]]
[[1 2]
 [3 4]]
[[0 1]
 [1 0]]
[[0 1]
 [1 0]]
[[2 1]
 [4 3]]
[[2 1]
 [4 3]]

'''