import numpy as np
from scipy import signal
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

t = np.arange(0, 10, 0.01)
r1 = np.c_[0.1*np.sin(0.9*np.sqrt(g/l)*t), np.zeros([len(t), 1])]
r2 = np.c_[0.1*np.sin(0.9*np.sqrt(g/l)*t), (0.9*np.sqrt(g/l))*0.1*np.cos(0.9*np.sqrt(g/l)*t)]

#Create an output vector: position, velocity, control
Cy = np.array([[1,0],[0,1],-K[0]]);
Dy = np.r_[np.zeros([2,2]), [K[0]]]

sys = signal.StateSpace(A-Bu*K, Bu*K, Cy, Dy);
tout1, y1, x1 = signal.lsim(sys, r1, t)
tout2, y2, x2 = signal.lsim(sys, r2, t)
#print(x1[:,1])

plt.figure()
plt.plot(t, y1[:,0])
plt.plot(t, y2[:,0])
plt.plot(t, r2[:,0])

plt.figure()
plt.plot(t, y1[:,1])
plt.plot(t, y2[:,1])
plt.plot(t, r1[:,1])
plt.plot(t, r2[:,1])

plt.figure()
plt.plot(t, y1[:,2])
plt.plot(t, y2[:,2])
plt.xlabel('time (s)')
plt.ylabel('Control Effort')
plt.savefig('controlplt.png', format='png', dpi=1000)