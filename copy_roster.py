#!/usr/bin/env python
import os 
import shutil
import time
### Purpose of this program is I need to send point cloud data to Hang 
### so can only send a small sample set because of time constraint 
### so we need to move all data from a roster to a seperte folder 

src_dir = "/data/city/nyc/pcd"
dst_dir = "/data/city/nyc/pcd60000"
# os.mkdir(dst_dir)

with open("/data/city/nyc/roster/common60000.txt", "r") as f:
    files = f.readlines()

files = [x.strip()+".npy" for x in files]

start = time.time()
for i, f in enumerate(files):
    if (i % 1000 == 0):
        print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    src_path = os.path.join(src_dir, f) 
    dst_path = os.path.join(dst_dir, f) 
    shutil.copy(src_path, dst_path)
