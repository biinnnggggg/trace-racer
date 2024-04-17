from .output import *
from .vec3d import *
from .interval import Interval

Color = Vec3D

def write_color(out : Output, pixel_color : Color) -> None:
    r = pixel_color.get_x()
    g = pixel_color.get_y()
    b = pixel_color.get_z()

    # translate the [0, 1] component values to the byte range [0, 255]
    intensity : Interval = Interval(0.000, 0.999)
    rbyte = int(255.999 * intensity.clamp(r))
    gbyte = int(255.999 * intensity.clamp(g))
    bbyte = int(255.999 * intensity.clamp(b))

    out.write(f'{rbyte} {gbyte} {bbyte}')
    