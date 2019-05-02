#!/usr/bin/env python
### 20190501
### Yuqiong Li
###  a program to log down names of all file in a directory and save to (multiple) .txt files
###  and do train-test-validation split

import os
import shutil
import time
import numpy as np


def list2file(l, path):
    """
    output a list to file.
    """
    with open(path, 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return


def train_val_test_split(l):
    """
    train validation test split of a list, 7:2:1
    :param l: the list to be split
    :return:
    """
    np.random.seed(1234)
    perm = np.random.permutation(len(l))
    train_id, val_id, test_id = np.split(perm, [int(.7 * len(l)), int(.9 * len(l))])
    train = [l[i] for i in train_id]
    test = [l[i] for i in test_id]
    val = [l[i] for i in val_id]
    return train, val, test

root = "/data/city/nyc/nyc_poly_binvox"
dst_dir = "/data/city/nyc/nyc_poly_binvox"+"_train_test_split"  # place to save .txt files
# root = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample"
# dst_dir = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample"+"_names"  # place to save .txt files
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

all_files = os.listdir(root)
train, val, test = train_val_test_split(all_files)

npath = os.path.join(dst_dir, "train.txt")
list2file(train, npath)
print("Train done!")

npath = os.path.join(dst_dir, "val.txt")
list2file(val, npath)
print("Val done!")

npath = os.path.join(dst_dir, "test.txt")
list2file(test, npath)
print("Test done!")
