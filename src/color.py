import numpy as np

from .output import *
from .interval import Interval

def process(pixel_color) -> tuple[int]:
    r, g, b = pixel_color

    rgb = (r, g, b)
    rgb = map(linear_to_gamma, rgb)
    
    intensity : Interval = Interval(0.000, 0.999)
    rgb = map(intensity.clamp, rgb)

    # translate the [0, 1] component values to the byte range [0, 255]
    rgb = map(lambda x : int(256 * x), rgb)
    return tuple(rgb)

def linear_to_gamma(linear_component : float) -> float:
    if linear_component > 0: return np.sqrt(linear_component)
    return 0