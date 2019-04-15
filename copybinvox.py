#!/usr/bin/env python
###  a program to move all finished binvox to another folder
import os 
import shutil
import time
# parent_dir = "/data/gmldata/nyc_objs/"
def list2file(l, name):
    """
    output a list to file.
    """
    with open(name+".txt", 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return

parent_dir = "/data/gmldata/nyc_finished_binvox"
dest_dir = "/data/gmldata/nyc_binvox_sample"
all_files = os.listdir(parent_dir)

start = time.time()
for i in range(100): 
    bid = all_files[i]
    # fpath = os.path.join(parent_dir, bid, "BuildingSurface.obj")
    # npath = os.path.join(dest_dir, bid+".obj")
    fpath = os.path.join(parent_dir, bid)
    npath = os.path.join(dest_dir, bid)
    shutil.copy(fpath, npath)
