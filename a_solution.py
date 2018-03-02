from operator import itemgetter

from utils import *
from random import randint, shuffle
from collections import defaultdict


def random_solution(nbr_rows: int, nbr_cols: int, nbr_cars: int, nbr_rides: int, bonus: int, max_t: int, rides: List[Ride])->Schedule:
    # print(nbr_rows, nbr_cols, nbr_cars, nbr_rides, bonus, max_t, rides)
    schedule = Schedule(nbr_cars=nbr_cars)
    for ride in rides:
        schedule.add_ride_to_car(ride=ride, car_num=randint(0, nbr_cars-1))
    return schedule


def greedy_solution(nbr_rows: int, nbr_cols: int, nbr_cars: int, nbr_rides: int, bonus: int, max_t: int, rides: List[Ride])->Schedule:

    car_next_free_list = [(car_num, 0, Pos(0, 0)) for car_num in range(nbr_cars)]
    done_cars = set()

    rides_set = set(rides)
    schedule = Schedule(nbr_cars=nbr_cars)

    last_len = 0
    while len(rides_set) and not len(done_cars) >= nbr_cars:
        if len(done_cars) != last_len:
            print(len(done_cars), '/', nbr_cars)
            last_len = len(done_cars)
        for car_num, t, pos in list(car_next_free_list):
            sorted_rides = sorted(rides_set, key=lambda ride: dist(pos, ride.sp))
            next_ = float('inf')
            for r in sorted_rides:
                arrival_time = dist(pos, r.sp)
                trip_time = arrival_time + dist(r.sp, r.ep)
                if t + arrival_time < next_:
                    next_ = t + arrival_time
                if t + arrival_time >= r.st and t + trip_time < r.et:
                    schedule.add_ride_to_car(car_num=car_num, ride=r)
                    rides_set.remove(r)
                    car_next_free_list[car_num] = (car_num, t + trip_time, r.ep)
                    # print(".", end=' ')
                    break
            else:
                # no ride assigned to car
                car_next_free_list[car_num] = (car_num, next_, pos)
                if t >= max_t:
                    done_cars.add(car_num)

    return schedule


def ridecentric_solution(nbr_rows: int, nbr_cols: int, nbr_cars: int, nbr_rides: int, bonus: int, max_t: int, rides: List[Ride])->Schedule:
    schedule = Schedule(nbr_cars=nbr_cars)

    d = defaultdict(set)
    car_next_free_set = set([(car_num, 0, Pos(0, 0)) for car_num in range(nbr_cars)])
    # for car_num in range(nbr_cars):
    #     d[Pos(0, 0)].add((car_num, 0))
    shuffle(rides)
    for ride in sorted(rides, key=lambda r: dist(Pos(0, 0), r.sp)):
        sorted_cars = sorted(car_next_free_set, key=lambda c: dist(ride.sp, c[2]) + c[1])
        for c in sorted_cars:
            num, t, cpos = c
            arrival = dist(cpos, ride.sp)
            triptime = dist(ride.sp, ride.ep)
            tot_time = t + arrival + triptime
            if t + arrival >= ride.st and tot_time < ride.et and tot_time < max_t:
                car_next_free_set.remove(c)
                car_next_free_set.add((num, tot_time, cpos))
                schedule.add_ride_to_car(ride, car_num=num)
                break

    return schedule
