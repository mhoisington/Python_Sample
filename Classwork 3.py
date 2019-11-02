import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import sqrt

m = 6e24
G = 6.8e-11
M = 2e30
x0 = 0
y0 = 1.5e11
vx0 = 3e4
vy0 = 0
tmax = 3.2e7
pts = 200

def Grav(xyvxvy,t):
    x,y,vx,vy = xyvxvy
    dxdt = vx
    dydt = vy
    dvdtx = (-G*M*x)/((sqrt(x**2+y**2))**3)
    dvdty = (-G*M*y)/((sqrt(x**2+y**2))**3)
    return dxdt,dydt,dvdtx,dvdty

t = np.linspace(0,tmax,pts)
y = odeint(Grav,(x0,y0,vx0,vy0),t)

plt.plot(t,y[:,0]/1e3,label='x')
plt.plot(t,y[:,1]/1e3,label='y')
plt.xlabel('Time (s)')
plt.ylabel('Position (km)')
plt.title('Orbit Position')
plt.figure()
plt.plot(t,y[:,2]/1e3,label='vx')
plt.plot(t,y[:,3]/1e3,label='vy')
plt.title('Orbit Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (km/s)')
plt.plot(y[:,0],y[:,1])
plt.legend()
plt.show()