# -*- coding:utf-8 -*-
'''
将文件中数据读入到np的matrix中
f1,f2,f3 ... fn,label
'''
import numpy as np
def file2NpMatrix(path):
    f=open(path,"r")
    lines=f.readlines() #返回值是list  [line1,line2,line3]
    row=len(lines)
    col=len(lines[0].split(","))
    returnMat=np.zeros((row,col))  #<type 'numpy.ndarray'>
    print type(returnMat)
    index=0
    for line in lines:
        returnMat[index, :] =(line.strip().split(","))
        index=index+1
    return np.mat(returnMat)

rMat=file2NpMatrix("F:\\python_code\\util\data\\1.txt")
print type(rMat)
print rMat
'''
[[  1.   2.   3.   4.   5.]
 [  6.   7.   8.   9.  10.]]
'''
