import matplotlib.pyplot as plt
import numpy as np

from figure_template import ScaleBar


# Generate date
# make these smaller to increase the resolution
dx, dy = 0.15, 0.05
# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(-3, 3 + dy, dy),
                slice(-3, 3 + dx, dx)]
z = (1 - x / 2. + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2) * np.sin(x)
# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()


fig = plt.figure()
ax = fig.add_subplot(111)

im = ax.imshow(z, cmap='RdBu', vmin=z_min, vmax=z_max,
           extent=[x.min(), x.max(), y.min(), y.max()],
           origin='lower')

rect_height = 0.05
rect_width = 1
padding = 3 * rect_height


fig.colorbar(im)

sb = ScaleBar(ax, label='100 nm', bar_length=0.8, padding=2)

ax.add_artist(sb)

plt.draw()

plt.show()
