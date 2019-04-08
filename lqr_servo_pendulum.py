import numpy as np
import control as c
#Define system matrices
g = 9.81
l=1
m=1
A = np.array([[0, 1], [-g/l, 0]])
Bu = np.array([[0], [1/m/(l^2)]])
#print(A)
#print(Bu)

#Set up LQR parameters/weights
R=0.001
Cz=np.diag([1, 1])
Rzz = np.diag([1, 0.1])
Q = np.transpose(Cz)*Rzz*Cz
#print(Cz)
#print(Rzz)
#print(Q)

K, S, E = c.lqr(A, Bu, Q, R)