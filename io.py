import sys
from utils import *

def read_data(fpath):
    f = open(fpath, 'r')
    data = f.readlines()

    R, C, F, N, B, T = data[0].split()

    rides = []
    for line in data[1:]:
        a, b, x, y, s, f = line.split()
        sp = Pos(a, b)
        ep = Pos(x, y)
        print(sp, ep, s, f)
        rides.append(Ride(s, f, sp, ep))

    return R, C, F, N, B, T, rides

read_data("./inputs/a_example.in")
