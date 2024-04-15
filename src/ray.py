from .vec3d import Vec3D, Point3D

class Ray:
    def __init__(self, pt : Point3D, dir : Vec3D) -> None:
        self.__pt = pt
        self.__dir = dir

    def at(self, t : float) -> Point3D:
        return self.__pt + (self.__dir * t)
