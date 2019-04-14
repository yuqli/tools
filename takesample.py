#!/usr/bin/env python
#### a program to sample a small number of files from a folder into another 
import os 
import shutil

src = "nyc_hmaps"
dst = "nyc_hmaps_tiny"
os.mkdir(dst)
allf = os.listdir(src)
for item in allf[0:11]:
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    shutil.copy(s, d)
