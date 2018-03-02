from inout import read_data, write_submission
from a_solution import *
from utils import compute_score
import time
import datetime

_d_e = ('d', 'e')
_a_to_c = ('a', 'b', 'c')
_all = _a_to_c + _d_e
inputs = _all

sum_score = 0
for input_ in inputs:
    start_t = time.time()
    # read input
    R, C, F, N, B, T, rides = read_data(input_)
    print("INPUT", input_)
    print("bonus", B)

    # find schedule
    schedule = ridecentric_solution(R, C, F, N, B, T, rides)

    # print score
    score = compute_score(schedule=schedule, bonus=B, max_t=T)
    # print('schedule', schedule)
    print('score', input_, ':', score)
    sum_score += score

    # create output
    write_submission(schedule.to_car_ride_nbrs(), out_name=f'{input_}_{score:,}')
    print(f'duration: {datetime.timedelta(seconds=time.time() - start_t)}')

print('total score', "{:,}".format(sum_score))
