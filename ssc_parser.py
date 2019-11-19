#! /usr/bin/python3

from pathlib import Path
import re
import random

from ssc import SSCFile

root = Path('.') / 'simfiles'
files = [x for x in root.iterdir() if x.suffix == '.ssc']
        

pat = re.compile(r'#(\w+):(.*?);', flags=re.DOTALL)
songs = list()
for file in files:
    with open(file) as f:
        matches = pat.findall(f.read())
        song = dict()
        song['charts'] = list()
        it = iter(matches)
        for key, value in it:
            if key == 'NOTEDATA': break
            song[key] = value.strip()
        chart = dict()
        for key, value in it:
            if key == 'NOTEDATA':
                song['charts'].append(chart)
                chart = dict()
                continue
            chart[key] = value.strip()
        ssc = SSCFile(song)
        songs.append(ssc)

with open('out.csv', 'w') as out:
    out.write('title,author,type,difficulty,taps,jumps,hands\n')
    for song in songs:
        for chart in song.charts:
            out.write(f'"{song.title}","{song.artist}","{chart.style}",'\
                      f'{chart.difficulty},{chart.taps},{chart.jumps},'\
                      f'{chart.hands}\n')

