#!/usr/bin/env python
### a program to find common point cloud and voxel data  
import os 

d1 = "/data/city/nyc/pcd"
d1 = "/data/city/nyc/vox64"

f1 = os.listdir(d1)
f2 = os.listdir(d2)

print("Old : {0}".format(len(f1)))
print("New : {0}".format(len(f2)))

common = set(f1) & set(f2)
print("Common : {0}".format(len(common)))
