import numpy as np
from numpy import pi,cos
import matplotlib.pyplot as plt
pts = 2000
f = np.linspace(10e3,25000e3,pts)
R = 33
V = 30
C = 12*(10**-9)
L = 150*(10**-6)
omega = f/(2*pi)
zl = omega*L*1j
zc = 1/(omega*C*1j)
zt = R + zl + zc
I = V/zt

plt.plot(f/1e3,I.real,c='c',label='I Real')
plt.plot(f/1e3,I.imag,'k,',label='I Imag')
plt.title('Current v. Frequency')
plt.ylabel('I (A)')
plt.xlabel('f (kHz)')
plt.legend()
plt.show()