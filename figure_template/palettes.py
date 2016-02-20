from collections import OrderedDict


class Pallete(OrderedDict):
    def to_normalized_rgb(self):
        for value in self:
            nr = self[value][0] / 255.0
            ng = self[value][1] / 255.0
            nb = self[value][2] / 255.0

            yield nr, ng, nb


# http://www.nature.com/nmeth/journal/v8/n6/full/nmeth.1618.html
seven_colors = Pallete([
    ('blue', (0, 114, 178)),
    ('orange', (230, 159, 0)),
    ('blueish_green', (0, 158, 115)),
    ('vermillion', (213, 94, 0)),
    ('sky_blue', (86, 180, 233)),
    ('yellow', (240, 228, 66)),
    ('reddish_purple', (204, 121, 167))
])
