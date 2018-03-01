from inout import read_data, write_submission
from a_solution import random_solution
from utils import compute_score

input_ = 'a'
# read input
R, C, F, N, B, T, rides = read_data(input_)

# find schedule
schedule = random_solution(R, C, F, N, B, T, rides)

# print score
score = compute_score(schedule=schedule, bonus=B, max_t=T)
print('score', score)

# create output
write_submission(schedule.to_car_ride_nbrs(), out_name=f'submission_{input_}')
