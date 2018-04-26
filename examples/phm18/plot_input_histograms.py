import numpy as np
import scipy
import scipy.interpolate as interp
from sklearn.neighbors import KernelDensity
from sklearn.grid_search import GridSearchCV
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import scipy.stats as st


title_font = {'fontname':'Arial', 'size':22, 'weight':'bold',
                            'verticalalignment':'bottom'}
axis_font = {'fontname':'Arial', 'size':35, 'weight':'normal'}
linez = ['--','-',':','-.']
colorz = ['r','g','b','k']

labelFont = 'Arial'
labelSize = 28
linewidth = 2.5
legendfont = 16.5
linewidth = 8

samplefile = "mc_data/input_samples_MC.txt"
samples = np.genfromtxt(samplefile)
n_samples = samples[:,2]
y_samples = samples[:,1]
c_samples = samples[:,0]

n_lims = [np.min(n_samples), np.max(n_samples)]
y_lims = [np.min(y_samples), np.max(y_samples)]
c_lims = [np.min(c_samples), np.max(c_samples)]


n_bins = 20
y_bins = 20
c_bins = 20

#Plot n:

fig = plt.figure()
ax = plt.subplot()

plt.hist(c_samples, color='cornflowerblue')

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname(labelFont)
    label.set_fontsize(labelSize)
plt.xlabel(r'$n$', **axis_font)
plt.ylabel("Frequency", **axis_font)
for label in ax.xaxis.get_ticklabels()[1::2]:
    label.set_visible(False)
plt.tight_layout()
plt.savefig("plots/n_hist.pdf")
plt.show()

#Plot y0:
fig = plt.figure()
ax = plt.subplot()

plt.hist(y_samples, color='cornflowerblue')

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname(labelFont)
    label.set_fontsize(labelSize)
plt.xlabel(r'$y_0$', **axis_font)
plt.ylabel("Frequency", **axis_font)
for label in ax.xaxis.get_ticklabels()[1::2]:
    label.set_visible(False)
plt.tight_layout()
plt.savefig("plots/y_hist.pdf")
plt.show()


#Plot C
fig = plt.figure()
ax = plt.subplot()

plt.hist(c_samples, color='cornflowerblue')

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname(labelFont)
    label.set_fontsize(labelSize)
plt.xlabel(r'log$C$', **axis_font)
plt.ylabel("Frequency", **axis_font)
for label in ax.xaxis.get_ticklabels()[1::2]:
    label.set_visible(False)
plt.tight_layout()
plt.savefig("plots/c_hist.pdf")
plt.show()


