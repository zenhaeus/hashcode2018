import sys
from utils import *

def read_data(in_data):
    examples = {
            'a' : 'a_example.in',
            'b' : 'b_should_be_easy.in',
            'c' : 'c_no_hurry.in',
            'd' : 'd_metropolis.in',
            'e' : 'e_high_bonus.in'
    }
    fpath = "./inputs/" + examples[in_data]

    f = open(fpath, 'r')
    data = f.readlines()

    R, C, F, N, B, T = data[0].split()

    rides = []
    for i, line in enumerate(data[1:]):
        a, b, x, y, s, f = line.split()
        sp = Pos(a, b)
        ep = Pos(x, y)
        rides.append(Ride(i, s, f, sp, ep))

    return R, C, F, N, B, T, rides

def write_submission(out_data):
    for car in out_data:
        print(len(car), end=" ")
        for ride in car:
            print(ride, end=" ")
        print()
