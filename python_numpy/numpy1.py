# -*- coding:utf-8 -*-
# /usr/bin/python
'''
@Author:  Yan Errol  @Email:2681506@gmail.com   
@Date:  2019-06-09  10:38
@Describe:numpy
@Evn:
'''

import numpy as np

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,3,4])[:,np.newaxis]
C = np.vstack((A,B))
D = np.hstack((A,B))

print(C,D)
print(A.shape,D.shape)
E = np.concatenate((A,B),axis=1)
print("E",E)

F = np.arange(12).reshape((3,4))
print("F",F)
print(np.split(F,3,axis=0))

A = np.array([1,1,1])
D = A
F = A.copy()
F[2] = 100
print("F",F)
print("A",A)
print("D",D)