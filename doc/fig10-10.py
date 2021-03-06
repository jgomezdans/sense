"""
comparison with figure 10-10 
in Ulaby 2014

- cross pol for Gaussian seems rather low

number of ittertaions??h


in general something with the Gaussian seems not to work yet!

quite o.k. for hv


"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

import numpy as np

from sense.surface import I2EM

import matplotlib.pyplot as plt

import time



def db(x):
    return 10.*np.log10(x)

start = time.time()
plt.close('all')


theta_deg = np.linspace(0.,70., 40)
theta = np.deg2rad(theta_deg)

f = plt.figure()
ax = f.add_subplot(111)


eps = 11.3-1.5j
f = 3.

s = 1./100.
l = 10./100.



hh1=[]
hh2=[]
vv1=[]
vv2=[]
hv1=[]
hv2=[]
xpol = True
auto=False
for t in theta:
    print t
    I1 = I2EM(f, eps, s, l, t, acf_type='gauss', xpol=xpol, auto=auto)
    I2 = I2EM(f, eps, s, l, t, acf_type='exp15', xpol=xpol, auto=auto)
    print I1.ks, I1.kl
    hh1.append(I1.hh)
    hh2.append(I2.hh)
    vv1.append(I1.vv)
    vv2.append(I2.vv)
    if xpol:
        hv1.append(I1.hv)
        hv2.append(I2.hv)

hh1 = np.array(hh1)
hh2 = np.array(hh2)
vv1 = np.array(vv1)
vv2 = np.array(vv2)
hv1 = np.array(hv1)
hv2 = np.array(hv2)

ax.plot(theta_deg, db(hh2), color='red', label='hh')
ax.plot(theta_deg, db(hh1), color='blue', label='hh')

ax.plot(theta_deg, db(vv2), color='red', label='vv', linestyle='--')
ax.plot(theta_deg, db(vv1), color='blue', label='vv', linestyle='--')

ax.plot(theta_deg, db(hv2), color='red', label='hv', linestyle='-.')
ax.plot(theta_deg, db(hv1), color='blue', label='hv', linestyle='-.')

ax.grid()
ax.set_xlim(0.,70.)
ax.set_ylim(-100.,30.)
print 'Elapsed time: ', time.time()-start
plt.show()
