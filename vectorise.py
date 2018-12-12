import sys
import pathlib
import re

import numpy as np

from collections import Counter, defaultdict

p = pathlib.Path(sys.argv[1])

subcorpora = defaultdict(list)

for d in p.iterdir():
    for f in d.glob("*"):
        with open(f) as in_stream:
            c = Counter(re.split(r"\W+", in_stream.read()))
            subcorpora[d.name].append(c)

voc = []
for s in subcorpora.values():
    for d in s:
        voc.extend(d.keys())

voc = sorted(set(voc))

if len(sys.argv) < 3:
    for n, s in subcorpora.items():
        with open(p / f"{n}.tsv", "w") as out_stream:
            for d in s:
                l = [str(d[word]) for word in voc]
                out_stream.write("\t".join(l) + "\n")
elif sys.argv[2] == "--relative":
    for n, s in subcorpora.items():
        with open(p / f"{n}.tsv", "w") as out_stream:
            for d in s:
                d_size = sum(d.values())
                l = [str(d[word] / d_size) for word in voc]
                out_stream.write("\t".join(l) + "\n")
elif sys.argv[2] == "--tfidf":
    docs = np.array(
        [
            [d[word] for word in voc]
            for s in sorted(subcorpora)
            for d in subcorpora[s]
        ]
    )
    tf = docs / np.sum(docs, axis=1, keepdims=True)
    idf = np.log(docs.shape[0] / np.count_nonzero(docs, axis=0))
    tfidf = tf * idf
    l = 0
    for n in sorted(subcorpora):
        breakpoint()
        np.savetxt(p / f"{n}.tsv", tfidf[l : len(subcorpora[n]), ...], delimiter="\t")
        l += len(subcorpora[n])
