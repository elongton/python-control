import numpy as np
from scipy import signal
import control
import matplotlib.pyplot as plt

L = 2
g = -10
d = 1
s = 1
M = 1
m = 1
k = 1

A = np.array([(0, 1, 0, 0), \
              (0, -d/M, -m*g/M, 0), \
              (0, 0, 0, 1), \
              (0, -s*d/(M*L)*k, -s*(m+M)*g, 0)])

B = np.array([(0),(1/M),(0),(s*1/(M*L))])




system = signal.lti([[0., 1.], [0., 0.]], [[0.], [1.]], [[1., 0.]], 0.)
t = np.linspace(0, 5)
u = np.ones_like(t)
tout, y, x = signal.lsim(system, u, t)

plt.plot(t, y)