from .vec3d import Vec3D, Point3D

class Ray:
    def __init__(self, pt : Point3D, dir : Vec3D) -> None:
        self.__pt = pt
        self.__dir = dir

    def get_origin(self) -> Point3D:
        return Vec3D.copy(self.__pt)

    def get_direction(self) -> Vec3D:
        return Vec3D.copy(self.__dir)

    def at(self, t : float) -> Point3D:
        return self.__pt + (self.__dir * t)
