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


def train_test_split(l):
    """
    train test split only, of a list, 7:2:1
    :param l: the list to be split
    :return:
    """
    np.random.seed(1234)
    perm = np.random.permutation(len(l))
    train_id, test_id = np.split(perm, [int(.85 * len(l))])
    train = [l[i] for i in train_id]
    test = [l[i] for i in test_id]
    return train, test


# root = "/data/city/nyc/nyc_poly_binvox"
# dst_dir = "/data/city/nyc/nyc_poly_binvox"+"_train_test_split"  # place to save .txt files
# with open("common100000.txt", "r") as f:
#     all = f.readlines()
root = "/media/yuqiong/DATA/city/shapenet/"
dst_dir = "/media/yuqiong/DATA/city/shapenet_catelog"  # place to save .txt files
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
allf = os.listdir(root)
allf = [x.strip() for x in allf]
# all_files = os.listdir(root)
# ids = np.random.choice(len(allf), 60000, replace=False)
# random_sample = [allf[x] for x in ids]

train, test = train_test_split(allf)

npath = os.path.join(dst_dir, "all.txt")
list2file(allf, npath)
print("Random Sample done!")

npath = os.path.join(dst_dir, "train.txt")
list2file(train, npath)
print("Train done!")

npath = os.path.join(dst_dir, "test.txt")
list2file(test, npath)
print("Test done!")
