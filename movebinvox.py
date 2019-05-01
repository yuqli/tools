#!/usr/bin/env python
###  a program to move all finished binvox to another folder
import os 
import shutil
import time


src_dir = "/data/city/nyc/nyc_poly_objs"
dst_dir = "/data/city/nyc/nyc_poly_binvox"
# src_dir = "/data/city/zurich/zurich_new_objs"
# dst_dir = "/data/city/zurich/zurich_binvox"

all_files = os.listdir(src_dir)

start = time.time()
for i in range(len(all_files)): 
    if (i % 1000 == 0):
        print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    bid = all_files[i]
    if bid.split(".")[1] == "binvox":
        fpath = os.path.join(src_dir, bid)
        npath = os.path.join(dst_dir, bid)
        shutil.move(fpath, npath)
