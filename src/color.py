from vec3d import Vec3D
from output import Output

Color = Vec3D

def write_color(out : Output, pixel_color : Color) -> None:
    r = pixel_color.get_x()
    g = pixel_color.get_y()
    b = pixel_color.get_z()

    # translate the [0, 1] component values to the byte range [0, 255]
    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    out.write(f'{rbyte} {gbyte} {bbyte}')
    