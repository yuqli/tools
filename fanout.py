#!/usr/bin/env python
### 20190430
### Yuqiong Li
###  a program to log down names of all file in a directory and save to (multiple) .txt files

import os
import shutil
import time
import numpy as np


def list2file(l, path):
    """
    output a list to file.
    """
    with open(path, 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return


def chunkify(lst,n):
    return [lst[i::n] for i in range(n)]

root = "/data/city/nyc/nyc_poly_binvox"
dst_dir = "/data/city/nyc/nyc_poly_binvox"+"_names"  # place to save .txt files
all_files = os.listdir(root)
num_children = 24   # number of copies to make
children = chunkify(all_files, num_children)

total_path = os.path.join(dst_dir, "all.txt")   # path to store all results
start = time.time()
for i in range(num_children):
    print("Child : {0}. Elapsed time: {1:.2f} min...".format(i, (time.time() - start) / 60))
    child = children[i]
    npath = os.path.join(dst_dir, "c{0}.txt".format(i))
    list2file(child, total_path)
    list2file(child, npath)

