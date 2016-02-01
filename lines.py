import numpy as np
import matplotlib.pyplot as plt

plt.style.use('~/code/python/py_figure_template/science.rc')


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

linestyles = ['-', '--', '-.', ':']

line1, = plt.plot(t, t**2, label='Line 1', color='crimson', linestyle=':')
line2, = plt.plot(t, np.sin(2*t), label='Line 2',color='royalblue', linestyle='-')
line3, = plt.plot(t, np.sin(2*t + 1) * t**2, label='Line 3',color='royalblue', linestyle='-.')


x_label = 'Time'
x_label_unit = 'seconds'


plt.xlabel('Time' + ' (')
plt.ylabel('Intensity (mW)')
plt.title('Happy plot')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 5, -1.1, 23])
plt.grid(True)
plt.legend()
plt.show()
