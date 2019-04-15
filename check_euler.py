#### 20190412
#### check in a given folder how many meshes are closed
import os
from argparse import ArgumentParser
from collections import deque


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


def check_euler(all_f):
    """
    check Euler‐Poincaré formula on a mesh's faces
    If a manifold is closed, then V + F - E = 2
    V : vertices
    F : faces
    E : edges
    http://graphics.stanford.edu/courses/cs468-10-fall/LectureSlides/02_Basics.pdf

    !!! Note: this algorithm is not every efficient as in counting edges it will
    compare every edge and see if it's already in the edges list ...
    BUT we can't have a set of set so this is the best I can come up at the moment
    """
    F = len(all_f)
    V = 0
    all_edges = [] # store all edges ...
    # iterate through all faces to count number of edges
    for f in all_f:
        items = deque(f)  # a method to rotate the list, faster than slicing
        items.rotate(-1)
        curr_edges = list(zip(f, list(items)))
        curr_edges = [set(x) for x in curr_edges]  # make edges unordered
        # print(curr_edges)
        for e in curr_edges:
            if e not in all_edges:
                all_edges.append(e)
        # print(all_edges)
        num = [int(x) for x in f]
        if max(num) > V:
            V = max(num)  # find the largest index of vertices, which is also number of vertices!
    E = len(all_edges)
    if V + F - E == 2:
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
    for file in files:
        path = os.path.join(folder, file)
        all_v, all_f = parse_obj(path)
        if check_euler(all_f) == True:
            valid_objs += 1
        else:
            invalid_objs += 1
    print("Valid objs:\t {0}".format(valid_objs))
    print("Invalid objs:\t {0}".format(invalid_objs))
    print("Done!")
    return


if __name__ == "__main__":
    main()
