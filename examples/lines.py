import numpy as np
import matplotlib.pyplot as plt
from figure_template import palettes
from cycler import cycler

plt.style.use('~/code/python/py_figure_template/science.rc')

# plt.rc('axes', prop_cycle=(cycler('color', [c for c in palettes.seven_colors.to_normalized_rgb()])))
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

linestyles = ['-', '--', '-.', ':']

line1, = plt.plot(t, t**2, label='Line 1')
line2, = plt.plot(t, np.sin(2*t), label='Line 2')
line3, = plt.plot(t, np.sin(2*t + 1) * t**2, label='Line 3')
line4, = plt.plot(t, np.sin(2*t + 1) * t**0.5, label='Line 3')
line5, = plt.plot(t, np.sin(2*t + 2) * t**2, label='Line 3')
line6, = plt.plot(t, np.sin(2*t + 3) * t**2, label='Line 3')


x_label = 'Time'
x_label_unit = 'second'


plt.xlabel('{0} ({1})'.format(x_label, x_label_unit))
plt.ylabel('Intensity (mW)')
plt.title('Happy plot')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 5, -6, 23])
plt.grid(True)
plt.legend()
plt.savefig('test.png')
plt.show()
