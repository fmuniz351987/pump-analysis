import re

STYLE_PAT = re.compile(r'pump-(\w+)')
TAP_PAT = re.compile(r'[124]')  # ha, tap_pat é um palíndromo :)


class Chart:
    def __init__(self, params):
        self.difficulty = params['METER']
        self.style = STYLE_PAT.search(params['STEPSTYPE']).group(1)
        self.raw_notes = params['NOTES']
        self.parse_notes()

    def parse_notes(self):
        self.taps = 0
        self.jumps = 0
        self.hands = 0
        for line in self.raw_notes.split('\n'):
            steps = len(TAP_PAT.findall(line))
            if steps == 0:
                pass
            elif steps == 1:
                self.taps += 1
            elif steps == 2:
                self.jumps += 1
            else:
                self.hands += 1

    def __repr__(self):
        return f'<Chart object {self.style}-{self.difficulty}, ' \
               f'{self.taps} taps, {self.jumps} jumps, {self.hands} hands>'

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, x):
        if x not in ('single', 'double', 'couple', 'routine', 'halfdouble'):
            raise ValueError(f'Style should be single or double, not {x}.')
        self.__style = x

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, x):
        self.__difficulty = int(x)

        
class SSCFile:
    def __init__(self, params):
        self.title = params['TITLE']
        self.artist = params['ARTIST']
        self.map_charts(params)

    def __repr__(self):
        return f'<SSCFile song: {self.title} by {self.artist}' \
               f'{self.charts}>'

    def map_charts(self, params):
        self.charts = list()
        for chart in params['charts']:
            try:
                self.charts.append(Chart(chart))
            except KeyError:
                pass
        self.n_charts = len(self.charts)

