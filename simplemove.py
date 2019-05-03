#!/usr/bin/env python
import os 
import shutil
import time
### Purpose of this program is the binvox program crashed as server crashed
### so some meshes are finished and others unfinished 
### so we need to move all .binvox files to the other folder 

src_dir = "/data/city/shapenet/"
dst_dir = "/data/city/data"

all_sub = os.listdir(src_dir)
start = time.time()
counter = 0
for sub in all_sub:
    subdir = os.path.join(src_dir, sub)
    allf= os.listdir(subdir)
    for f in allf:
        if (counter % 1000 == 0):
            print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(counter, (time.time() - start)/60))
        src_path = os.path.join(subdir, f) 
        dst_path = os.path.join(dst_dir, f) 
        shutil.move(src_path, dst_path)
        counter += 1
