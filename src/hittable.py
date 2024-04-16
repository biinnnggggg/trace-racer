import numpy as np

from .ray import Ray
from .vec3d import Vec3D, Point3D

class HitRecord:
    def __init__(self, p : Point3D=None, norm : Vec3D=None, t : float=None):
        self.p = p
        self.norm = norm
        self.t = t

class Hittable:
    """An abstract class all 'hittable' objects inherit from
    """
    def hit(self, ray : Ray, t_min : float, t_max : float, hit_record : HitRecord) -> bool:
        raise NotImplementedError

class Sphere(Hittable):
    def __init__(self, center : Point3D, radius : float):
        self.__center = center
        self.__radius = radius

    def hit(self, ray : Ray, t_min : float, t_max : float, record : HitRecord) -> bool:
        q = ray.get_origin()
        d = ray.get_direction()

        a = d.dot(d)
        h = d.dot(self.__center - q)
        x = q - self.__center
        c = x.dot(x) - self.__radius * self.__radius

        discriminant = h * h - a * c
        
        if discriminant < 0: 
            return False
        
        sqrt_result = np.sqrt(discriminant)

        t1 = (h - sqrt_result) / a
        t2 = (h + sqrt_result) / a
        
        t = None
        if t_min <= t2 <= t_max:
            t = t2
        
        # take negative since 'forward' is -z
        if t_min <= t1 <= t_max:
            t = t1
        
        if t is None:
            return False
        
        record.p = ray.at(t)
        record.norm = (record.p - self.__center) / self.__radius
        record.t = t

        return True