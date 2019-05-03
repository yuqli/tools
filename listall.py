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

root = "/data/city/nyc/vox64"
dst_dir = "/data/city/nyc/vox64"+"_names"  # place to save .txt files
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

all_files = os.listdir(root)
total_path = os.path.join(dst_dir, "all.txt")   # path to store all results
list2file(all_files, total_path)
