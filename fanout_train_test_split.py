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

def sample_n(l, n):
    """
    randomly sample n objects from list l
    """
    np.random.seed(1234)
    ids = np.random.choice(len(l), n, replace=False)
    return [l[x] for x in ids]


def train_test_split(l):
    """
    train test split of a list, 9:1
    :param l: the list to be split
    :return:
    """
    np.random.seed(1234)
    perm = np.random.permutation(len(l))
    train_id, test_id = np.split(perm, [int(.85 * len(l))])
    train = [l[i] for i in train_id]
    test = [l[i] for i in test_id]
    return train, test

root = "/data/city/nyc/vox64"
dst_dir = root + "_train_test_split"  # place to save .txt files

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

all_files = os.listdir(root)
sample = sample_n(all_files, 60000) 
# train, val, test = train_val_test_split(all_files)
train, test = train_test_split(sample)

npath = os.path.join(dst_dir, "sample.txt")
list2file(sample, npath)
print("All sample done!")

npath = os.path.join(dst_dir, "train.txt")
list2file(train, npath)
print("Train done!")

#npath = os.path.join(dst_dir, "val.txt")
#list2file(val, npath)
#print("Val done!")

npath = os.path.join(dst_dir, "test.txt")
list2file(test, npath)
print("Test done!")
