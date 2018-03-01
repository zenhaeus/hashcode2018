from typing import Generator, Iterable, List
from collections import namedtuple

Pos = namedtuple('Pos', ['r', 'c'])
Ride = namedtuple('Ride', ['st' 'et', 'sp', 'ep'])


class CompletedRide(namedtuple('CompletedR', ['ride', 'pt', 'dt'])):  # pickup time, deliver time

    def __init__(self, ride: Ride, pt: int, dt: int):
        assert isinstance(ride, Ride)
        assert isinstance(pt, int)
        assert isinstance(dt, int)

    def score(self):
        if self.ride.et <= self.dt:
            return 0
        return dist(self.ride.st, self.ride.et) + (2 if self.pt == self.ride.st else 0)


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


def compute_score_completed_rides(completed_rides: List[CompletedRide]):
    return sum(cr.score() for cr in completed_rides)

