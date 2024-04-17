import numpy as np 

# Constants
INF : float = 10e12
PI : float = 3.1415926535897932385

RNG = np.random.default_rng()

# Utility functions

def deg_to_rad(degrees : float) -> float:
    """Converts an angle from degrees to radians.
    """
    return degrees * PI / 180.0

def rand_float() -> float:
    """Returns a random float in [0, 1)
    """
    return RNG.random()

def rand_float_in(a : float, b : float) -> float:
    """Returns a random float in [a, b)
    """
    return (b - a) * RNG.random() + a