import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,sqrt
from scipy.optimize import curve_fit

data = np.loadtxt("wavedata.txt",float,skiprows=1)
t = data[:,0]
y = data[:,1]
sigma = np.ones(len(t))

def f(x,p0,p1,p2,p3):
    return p0 + p1*sin((p2*x)-p3)

(p0,p1,p2,p3),cc = curve_fit(f,t,y)
tmod = np.linspace(t[0],t[-1],100)
ymod = f(tmod,p0,p1,p2,p3)

plt.plot(t,y)
plt.plot(tmod,ymod)
plt.title('sin(t) v. t')
plt.xlabel('t')
plt.ylabel('sin(t)')
plt.show()

p = 4
fdat = f(t,p0,p1,p2,p3)
diffs = (y-fdat)**2/sigma**2
dof = len(t)-p
chisqr = sum(diffs)/dof
print('Redcued chi-squared:',chisqr)

up0,up1,up2,up3 = 2*sqrt(np.diag(cc))
print()
print('Two-sigma uncertainties:')
print()
print('p0:',p0,'+/-',up0)
print('p1:',p1,'+/-',up1)
print('p2:',p2,'+/-',up2)
print('p3:',p3,'+/-',up3)