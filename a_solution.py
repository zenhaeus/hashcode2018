from typing import List

from utils import *
from random import randint


def random_solution(nbr_rows: int, nbr_cols: int, nbr_cars: int, nbr_rides: int, bonus: int, max_t: int, rides: List[Ride])->Schedule:
    schedule = Schedule(nbr_cars=nbr_cars)
    for ride in rides:
        schedule.add_ride_to_car(ride=ride, car_num=randint(0, nbr_cars))
    print()
    return schedule
