#!/usr/bin/env python
# produces a summary of a folder: how many files, in which how many folders
import os 
import shutil
import time
import numpy as np
from scipy import stats
parent_dir = "/data/city/nyc/nyc_triangle_objs"

all_files = os.listdir(parent_dir)
print("Number of files: {0}".format(len(all_files)))

folder_counter = 0
folder_size_list = []

for f in all_files:
    curr_path = os.path.join(parent_dir, f)
    if os.path.isdir(curr_path):
        folder_counter += 1
        sub_files = os.listdir(curr_path)
        folder_size_list.append(len(sub_files))
sub = np.array(folder_size_list)

print("Number of directories: {0}".format(folder_counter))
print("Number of non-directories: {0}".format(len(all_files) - folder_counter))
stats.describe(sub)
