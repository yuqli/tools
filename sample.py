#!/usr/bin/env python
import os 
import shutil
import time
import numpy as np

### This program samples a few files from a parent directory so we can inspect and visualize
# parent_dir = "/data/city/nyc/nyc_triangle_objs"
parent_dir = "/data/city/nyc/nyc_tri_pcds_4096"
sample_dir = parent_dir + "_sample" 
if not os.path.exists(sample_dir):
    os.mkdir(sample_dir)

all_files = os.listdir(parent_dir)
num_sample = 1000
sample_ids = np.random.choice(len(all_files), num_sample) 

for i in sample_ids:
    f = all_files[i]
    src_path = os.path.join(parent_dir, f)
    dst_path = os.path.join(sample_dir, f)
    if not os.path.isdir(src_path):
        shutil.copy(src_path, dst_path)

