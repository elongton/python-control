import numpy as np
#from scipy import signal
import sympy as sym
#import control
#import matplotlib.pyplot as plt

s = sym.Symbol('s');

m = 1
k = 1
c = 2

A = np.array([[0, 1], [-k/m, -c/m]])
B = np.array([[0, 0, 0], [1/m, 1/m, 0]])
C = np.array([0, 1])
D = np.array([0,0,1])

#print(s)
#tf = signal.ss2tf(A, B, C, D, 0)
#print(s*np.eye(2,2)-A)
#print(np.linalg.inv(s*np.eye(2,2)-A))
#tf2 = C*(np.linalg.inv(np.eye(2,2)-A))*B + np.transpose(D)
#print(np.linalg.inv(A))

#print(s*np.eye(2,2))
#print(tf2)


print(C.dot((s*np.eye(2,2)-A).dot(B))+D)