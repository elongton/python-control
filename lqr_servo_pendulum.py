import numpy as np
import control as c
import matplotlib.pyplot as plt
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

t = np.arange(0, 10, 0.1)
#r1 = [0.1*np.sin(0.9*np.sqrt(g/l)*np.transpose(t)), np.zeros(len(t), 1)];
r11 = 0.1*np.sin(0.9*np.sqrt(g/l)*np.transpose(t))
#print(r11)

plt.plot(t, r11)