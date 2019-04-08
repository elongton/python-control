import numpy as np
from scipy import signal
import sympy as sym
#import control
#import matplotlib.pyplot as plt

s = sym.Symbol('s');

m = 1
k = 1
c = 2

A = np.array([[0, 1], [-k/m, -c/m]])
B = np.array([[0, 0], [1/m, 1/m]])
C = np.array([0, 1])
D = np.array([1, 1])

#print(s)
#tf = signal.StateSpace(C*np.linalg.inv(s*np.eye(2,2)-A)*B)
#print(s*np.eye(2,2)-A)
#print(np.linalg.inv(s*np.eye(2,2)-A))

print(np.linalg.inv(A))

print(s*np.eye(2,2))
print(np.linalg.inv(s*np.eye(2,2)))