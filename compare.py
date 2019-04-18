#!/usr/bin/env python
### a program to compare how many files in two directories are the same 
import os 

d1 = "/media/yuqiong/DATA/city/zurich/zurich_building_objs"
d2 = "/media/yuqiong/DATA/city/zurich/zurich_new_objs"

f1 = os.listdir(d1)
f2 = os.listdir(d2)

print("Old : {0}".format(len(f1)))
print("New : {0}".format(len(f2)))

common = set(f1) & set(f2)
print("Common : {0}".format(len(common)))