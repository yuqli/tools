#!/usr/bin/env python
import os 
import shutil
import time
### Purpose of this program is the binvox program crashed as server crashed
### so some meshes are finished and others unfinished 
### so we need to move all .binvox files to the other folder 

src_dir = "/data/city/nyc/tmp/nyc_poly_binvox_64_cuda"
dst_dir = "/data/city/nyc/nyc_poly_binvox_64_cuda"

all_files = os.listdir(src_dir)
start = time.time()
for i, f in enumerate(all_files):
    if (i % 1000 == 0):
        print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    src_path = os.path.join(src_dir, f) 
    dst_path = os.path.join(dst_dir, f) 
    shutil.move(src_path, dst_path)
