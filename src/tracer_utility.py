import numpy as np

# Common modules
from .color import *
from .ray import *
from .vec3d import *
from .output import *

# Constants
INF : float = 10e12
PI : float = 3.1415926535897932385

# Utility functions

def degrees_to_radian(degrees : float) -> float:
    return degrees * PI / 180.0
