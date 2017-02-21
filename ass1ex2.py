import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

#theta''(t) + b*theta'(t) + c*sin(theta(t)) = 0
Om = 0.8
Ol = 0.2
H0 = 7e4
G = 6.67e-11
rho_crit = 3*H0**2/(8*pi*G)
rho_0 = Om*rho_crit

a = 1e-3
H = H0*sqrt(Om*a**-3+Ol)
#def b(a)
b = H0/H**2*(Ol-Om/2*a**-3)-3+a**2/H+H**-1
c = 4*np.pi*G*rho_0



#theta'(t) = omega(t)
#omega'(t) = -b*omega(t) - c*sin(theta(t))

def pend(y, t, b, c):
	theta, omega = y
	dydt = [omega, -b*omega - c*np.sin(theta)]
	return dydt

y0 = [np.pi - 0.1, 0.0]
a = np.linspace(0, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
