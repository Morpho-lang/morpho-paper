import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import argrelextrema, iirfilter, sosfilt, find_peaks

plt.style.use("paper.mplstyle")
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

plt.figure(figsize=(3.71,2))

data = np.loadtxt("curvature.txt")
ln = data[:,0]
en = data[:,1]
order = data[:,2].astype(int)
en = en[list(order)]
x = np.cumsum(ln)
fs=1/(x[1]-x[0])
length = x[-1]
x /= x[-1]
ms = find_peaks(en,  prominence=0.01)[0]

plt.plot(x, en)
for m in ms:
    plt.plot(x[m], en[m], 'o', color='k')
(yl, yh) = plt.ylim()
plt.ylim((1,yh))
plt.xlim((0,1))
plt.xlabel(r"$\tilde{s}$")
plt.ylabel(r"$\tilde{\chi}(\tilde{s})$")
ax = plt.gca()
ax.tick_params(direction="in")
ax.tick_params(which="minor", direction="in")
plt.tight_layout()
plt.savefig("curvature.pdf")
plt.show()
