#### 20190418
#### check in a given folder how many faces
import os
from argparse import ArgumentParser
from collections import deque
from timeit import default_timer as timer
from datetime import timedelta
import gc

def parse_obj(path):
    """
    a function to read and parse obj files
    @ param path: absolute path to obj file
    """
    with open(path) as fp:
        lines = fp.readlines()
    lines = [x for x in lines if x[0] != '#']
    all_v = [x.split(' ')[1:] for x in lines if x[0] == 'v'] # all verices
    all_f = [x.split(' ')[1:] for x in lines if x[0] == 'f'] # all verices
    return all_v, all_f


def check_flat(all_f):
    """
    check in a polygon mesh how many faces are there
    this is to rule out potential bad data with LoD1 information
    """
    if len(all_f) == 1:
        return True
    else:
        return False

def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--folder",
                        help="the folder containing .obj files")
    parser.add_argument("-q", "--quiet",
                        action="store_false", default=True,
                        help="don't print status messages to stdout")
    args = parser.parse_args()

    folder = args.folder
    print(folder)
    files = os.listdir(folder)
    valid_objs = 0
    invalid_objs = 0
    counter = 0
    
    start = timer()
    
    for file in files:
        path = os.path.join(folder, file)
        all_v, all_f = parse_obj(path)
        if check_flat(all_f) == True:
            invalid_objs += 1
        else:
            valid_objs += 1
        if counter % 1000 == 0:
            print("Number of files :\t {0}".format(counter))
            print("Valid objs:\t {0}".format(valid_objs))
            print("Invalid objs:\t {0}".format(invalid_objs))
            end = timer()
            print("Time elapsed: {0}".format(timedelta(seconds=end-start)))
            gc.collect()
        counter += 1
    print("Done!")
    return


if __name__ == "__main__":
    main()
