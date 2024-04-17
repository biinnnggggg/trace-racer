from .vec3d import Point3D, Vec3D

class Ray:
    """Represents a ray.
    """
    def __init__(self, pt : Point3D, dir : Vec3D) -> None:
        self.__pt = pt
        self.__dir = dir

    def get_origin(self) -> Point3D:
        """Returns the origin of the ray.
        """
        return Vec3D.copy(self.__pt)

    def get_direction(self) -> Vec3D:
        """Returns the direction of the ray as a vector.
        """
        return Vec3D.copy(self.__dir)

    def at(self, t : float) -> Point3D:
        """Returns the point along the ray at step t.
        """
        return self.__pt + (self.__dir * t)
