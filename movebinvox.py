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

parent_dir = "/data/gmldata/nyc_objs_organized"
dest_dir = "/data/gmldata/nyc_objs_sample"
all_files = os.listdir(parent_dir)
all_ids = [x for x in all_files if len(x.split("."))==1]
print(len(all_ids))
fname = "/data/gmldata/nyc_obj_indices"
list2file(all_ids, fname)

sample_files = all_files[:2000]

start = time.time()
for i in range(len(sample_files)): 
    if (i % 100 == 0):
        print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    bid = sample_files[i]
    # fpath = os.path.join(parent_dir, bid, "BuildingSurface.obj")
    # npath = os.path.join(dest_dir, bid+".obj")
    fpath = os.path.join(parent_dir, bid)
    npath = os.path.join(dest_dir, bid)
    shutil.copy(fpath, npath)
