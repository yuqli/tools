#!/usr/bin/env python
###  a program to move all finished binvox to another folder
import os 
import shutil
import time

def list2file(l, name):
    """
    output a list to file.
    """
    with open(name+".txt", 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return

src_dir = "/data/city/nyc/nyc_mesh_undo"
dst_dir = "/data/city/nyc/nyc_binvox"

all_files = os.listdir(dst_dir)

start = time.time()
for i in range(len(all_files)): 
    if (i % 100 == 0):
        print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    bid = all_files[i]
    if bid.split(".")[1] == "obj":
        fpath = os.path.join(src_dir, bid)
        npath = os.path.join(dst_dir, bid)
        shutil.move(npath, fpath)
