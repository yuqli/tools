#!/usr/bin/env python
import os 
import shutil
import time

### this program is to move and split all building obj files for NYC. There are around one million of them.

parent_dir = "/data/gmldata/nyc_finished_binvox"

for i in range(4):
    os.mkdir(parent_dir + "_" + str(i)) 

all_files = os.listdir(parent_dir)
start = time.time()
for i, f in enumerate(all_files):
    print("Now checking the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    dst_id = i % 4
    dst_folder = parent_dir + "_" +  str(dst_id)
    src_path = os.path.join(parent_dir, f)
    dst_path = os.path.join(dst_folder, f)
    shutil.move(src_path, dst_path)

