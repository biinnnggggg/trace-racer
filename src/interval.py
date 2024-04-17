from .tracer_utility import INF

class Interval:
    empty = None
    universe = None

    def __init__(self, min : float, max : float) -> None:
        self.min = min
        self.max = max

    def size(self) -> float:
        return self.max - self.min

    def surrounds(self, x : float) -> bool:
        return self.min < x < self.max
    
    def contains(self, x : float) -> bool:
        return self.min <= x <= self.max

Interval.empty = Interval(INF, -INF)
Interval.universe = Interval(-INF, INF)