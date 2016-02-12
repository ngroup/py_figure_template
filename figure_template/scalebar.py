import matplotlib.patches as mpatches
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, VPacker,\
    TextArea
from matplotlib import rcParams

class ScaleBar(AnchoredOffsetbox):
    def __init__(self, ax, label, bar_length, **props):
        '''
        Draw a horizontal bar with the size in data coordinate of the give axes.
        A label will be drawn above (center-aligned).
        '''
        label_size = props['label_size'] if 'label_size' in props else \
            rcParams.get('scalebar.label_size', 16)
        label_family = props['label_family'] if 'label_family' in props else \
            rcParams.get('scalebar.label_family', 'sans-serif')
        label_color = props['label_color'] if 'label_color' in props else \
            rcParams.get('scalebar.label_color', 'black')
        location = props['location'] if 'location' in props else \
            rcParams.get('scalebar.location', 4)
        padding = props['padding'] if 'padding' in props else \
            rcParams.get('scalebar.padding', 0.5)
        sep = props['sep'] if 'sep' in props else \
            rcParams.get('scalebar.sep', 2)
        bar_color = props['bar_color'] if 'bar_color' in props else \
            rcParams.get('scalebar.bar_color', 'black')
        bar_width = props['bar_width'] if 'bar_width' in props else \
            rcParams.get('scalebar.bar_width', 0.1)
        bar_length = props['bar_length'] if 'bar_length' in props else \
            rcParams.get('scalebar.bar_length', 0.8)

        frameon = False
        prop = None

        self.scale_bar = AuxTransformBox(ax.transData)


        rect = mpatches.Rectangle((0, 0),
                          bar_length, bar_width,
                          linewidth=0, edgecolor=None,
                          facecolor=bar_color)

        self.scale_bar.add_artist(rect)

        textprops = {'size': label_size}

        self.txt_label = TextArea(label, textprops=textprops, minimumdescent=False)

        self._box = VPacker(children=[self.txt_label, self.scale_bar],
                            align="center",
                            pad=0, sep=sep)

        AnchoredOffsetbox.__init__(self, location, pad=padding, borderpad=0,
                                   child=self._box,
                                   prop=prop,
                                   frameon=frameon)
