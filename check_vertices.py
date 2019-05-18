#### 20190412
#### check in a given folder how many meshes are closed
import os
from argparse import ArgumentParser
from collections import deque
import pandas as pd

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
    total = []
    for i, f in enumerate(files):
        res = {}
        if i % 1000 == 0 and i != 0:
            print("Processing the {0}-th file...\n".format(i))
            df = pd.DataFrame(total)
            with open("vertice_result1.csv", 'a') as io:
                df.to_csv(io, header=True)
            total = []
        res["file"] = f
        print(folder)
        print(f)
        path = os.path.join(folder, f)
        print(path)
        all_v, all_f = parse_obj(path)
        res["v"] = len(all_v)
        res["f"] = len(all_f)
        total.append(res)
    print("Done!")
    return


if __name__ == "__main__":
    main()
