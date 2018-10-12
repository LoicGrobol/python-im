import sys
import re
import json

def code_cell(content):
    content = content.strip()
    if content.startswith("```python3"):
        content = content[10 : ]
    elif content.startswith("```"):
        content = content[3 : ]
    if content.endswith("```"):
        content = content[ : -3]
    content = content.strip()
    parts = [s+"\n" for s in content.split("\n")]
    parts[-1] = parts[-1].rstrip()
    return {"cell_type": "code", "execution_count": None, "metadata": {"slideshow": {"slide_type": "-"}}, "outputs": [], "source": parts}

def md_cell(content):
    content = re.sub("<.+?>", "", content.strip())
    parts = [s+"\n" for s in content.split("\n")]
    return {"cell_type": "markdown", "source": parts, "metadata": {"slideshow": {"slide_type": "slide"}}}

def cells(content):
    content = re.sub("<.+?>", "", content.strip())
    indx = 0
    parts = []
    for match in re.finditer("```python3?.+?```", content, flags=re.M + re.DOTALL):
        start, end = match.span()
        parts.append(content[indx : start])
        parts.append(content[start : end])
        indx = end
    parts.append(content[indx : ])
    parts = [p.strip() for p in parts if p.strip()]
    lst = []
    for part in parts:
        if part.startswith("```"):
            lst.append(code_cell(part))
        else:
            lst.append(md_cell(part))
    for item in lst[1:]:
        item["metadata"]["slideshow"]["slide_type"] = "-"
    return lst

name = sys.argv[1]
outname = name.rsplit(".", 1)[0] + ".ipynb"

with open(name, "rU", newline="", encoding="utf-8") as ifd:
    content = ifd.read()
    content = re.search("<textarea.+?>(.+?)</textarea>", content, flags=re.M + re.DOTALL).group(1)

ipynb = {
  "cells": [],
  "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  },
  "livereveal": {
   "autolaunch": True,
   "scroll": True,
   "transition": "none"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

for cell_content in content.split("---"):
    ipynb["cells"].extend(cells(cell_content))

with open(outname, "w") as ofd:
    json.dump(ipynb, ofd, ensure_ascii=False, indent=2)
