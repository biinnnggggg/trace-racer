from .output import *
from .vec3d import *
from .interval import Interval

Color = Vec3D

def process(pixel_color : Color) -> tuple[int]:
    r = pixel_color.get_x()
    g = pixel_color.get_y()
    b = pixel_color.get_z()

    # translate the [0, 1] component values to the byte range [0, 255]
    intensity : Interval = Interval(0.000, 0.999)
    r = int(255.999 * intensity.clamp(r))
    g = int(255.999 * intensity.clamp(g))
    b = int(255.999 * intensity.clamp(b))

    return (r, g, b)