from .tracer_utility import INF

class Interval:
    """Represents an interval of values.
    """
    empty = None
    universe = None

    def __init__(self, min : float, max : float) -> None:
        self.min = min
        self.max = max

    def size(self) -> float:
        """Returns the size of the interval as the difference of the endpoints.
        """
        return self.max - self.min

    def surrounds(self, x : float) -> bool:
        """Returns True if the parameter x is in the interval exclusive of
        endpoints, and False otherwise.
        """
        return self.min < x < self.max
    
    def clamp(self, x : float) -> float:
        """Returns the nearest value in the interval to the parameter x.
        """
        if x < self.min: return self.min
        if x > self.max: return self.max
        return x
    
    def contains(self, x : float) -> bool:
        """Returns True if the parameter x is in the interval inclusive of
        endpoints, and False otherwise.
        """
        return self.min <= x <= self.max

Interval.empty = Interval(INF, -INF)
Interval.universe = Interval(-INF, INF)