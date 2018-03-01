from typing import Generator, Iterable, List
from collections import namedtuple

Pos = namedtuple('Pos', ['r', 'c'])
Ride = namedtuple('Ride', ['st', 'et', 'sp', 'ep'])


class CompletedRide(namedtuple('CompletedR', ['ride', 'pt', 'dt'])):  # pickup time, deliver time

    def __init__(self, ride: Ride, pt: int, dt: int):
        assert isinstance(ride, Ride)
        assert isinstance(pt, int)
        assert isinstance(dt, int)

    def score(self, max_t: int):
        if self.ride.et <= self.dt or self.ride.et > max_t:
            return 0
        return dist(self.ride.st, self.ride.et) + (2 if self.pt == self.ride.st else 0)


class Schedule:

    def __init__(self, nbr_cars: int):
        self.car_list: List[List[Ride]] = [list() for _ in range(nbr_cars)]

    def schedule_of_car(self, num: int):
        return self.car_list[num]

    def add_ride_to_car(self, ride: Ride, car_num: int):
        self.car_list[car_num].append(ride)

    def to_completed_rides(self, cars_start_pos: Pos=Pos(0, 0))->List[CompletedRide]:
        """
        Takes all sheduled rides and executes them
        :return: List of all completed rides in the schedule
        """
        completed_rides = list()
        for cl in self.car_list:
            cpos = cars_start_pos
            _t = 0
            for ride in cl:
                _t += dist(cpos, ride.sp)
                pt = _t  # pickup time
                _t += dist(ride.sp, ride.ep)
                dt = _t # delivery time
                completed_rides.append(CompletedRide(ride=ride, pt=pt, dt=dt))
                cpos = ride.ep  # update position

        return completed_rides


def flatten(l: Iterable)->List:
    """

    :param l:
    :return: a list containing the flattened iterable
    """
    return list(flatten_gen(l))


def flatten_gen(l: Iterable)->Generator:
    """
    >>> list(flatten([]))
    []
    >>> list(flatten([[], [[], []]]))
    []

    >>> list(flatten_gen([1, 2, 3, 4]))
    [1, 2, 3, 4]

    >>> list(flatten_gen([1, 2, [3, 4], 5]))
    [1, 2, 3, 4, 5]

    >>> list(flatten_gen([[1, [2, [3, 4]], 5]]))
    [1, 2, 3, 4, 5]

    >>> list(flatten_gen([[1, [2, [3, 4, 'abd']], 5]]))
    [1, 2, 3, 4, 'abd', 5]

    Flattens the given (nested) list.
    Note: Consumes the given iterable if it is a generator.
    :param l:
    :return: a generator generating each element of the flattened list
    """
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten_gen(el)
        else:
            yield el


def dist(pos1: Pos, pos2: Pos)->float:
    return abs(pos1.r - pos2.r) + abs(pos1.c - pos2.c)


def compute_score(schedule: Schedule, max_t: int)->int:
    return compute_score_completed_rides(schedule.to_completed_rides(), max_t=max_t)


def compute_score_completed_rides(completed_rides: List[CompletedRide], max_t: int)->int:
    return sum(cr.score(max_t=max_t) for cr in completed_rides)

