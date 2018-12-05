import sys
import pathlib
import re

from collections import Counter

p = pathlib.Path(sys.argv[1])

file_dicts = []

for f in p.glob('*'):
    with open(f) as in_stream:
        d = Counter(re.split(r'\W+', in_stream.read()))
        file_dicts.append(d)

voc = []
for d in file_dicts:
    voc.extend(d.keys())

voc = sorted(set(voc))

for d in file_dicts:
    l = [str(d[word]) for word in voc]
    print('\t'.join(l))
