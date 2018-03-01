import sys
import datetime as dt

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

    R, C, F, N, B, T = map(int, data[0].split())

    rides = []
    for i, line in enumerate(data[1:]):
        a, b, x, y, s, f = map(int, line.split())
        sp = Pos(a, b)
        ep = Pos(x, y)
        rides.append(Ride(i, s, f, sp, ep))

    return R, C, F, N, B, T, rides


def write_submission(out_data, out_name="submission"):
    f = open("./outputs/{}_{}.out".format(out_name, dt.datetime.today().replace(microsecond=0)), 'w')
    for car in out_data:
        f.write(str(len(car)) + " ")
        for ride in car:
            f.write(str(ride) + " ")
        f.write('\n')
    f.close()

"""
sample_out = [
        [0, 1, 2],
        [2, 4],
        [2, 6, 7, 1]
]
write_submission(sample_out)
"""
