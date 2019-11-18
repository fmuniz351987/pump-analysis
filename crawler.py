#! /usr/bin/python3

from pathlib import Path
import shutil

extensions = ['ssc', 'sm']

root = Path(input())

if not (root.exists() and root.is_dir()):
    raise FileNotFoundError('Please insert a valid directory to search on.')

simfiles = []

for ext in extensions:
    files = root.glob('**/*.' + ext)
    simfiles += files

for file in simfiles:
    print(file.name)

songs_out = Path('.') / 'simfiles'
songs_out.mkdir()

for file in simfiles:
	try:
	    shutil.copyfile(file, songs_out / file.name)
	except shutil.SameFileError:
		pass
