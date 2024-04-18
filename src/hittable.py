from .tracer_utility import *
from .interval import Interval

class HitRecord:
    """Records information about Ray and Hittable object intersection.
    """
    def __init__(self,
                 p=None,
                 normal=None,
                 t : float=None,
                 front_face : bool=None) -> None:
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face
        self.mat = None

    def set_face_normal(self, pt, dr, outward_normal) -> None:
        """Sets the hit record normal vector. Note that the parameter
        `outward_normal` is assumed to have unit length.
        """
        assert np.isclose(np.linalg.norm(outward_normal), 1.0)
        self.front_face = dr.dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable:
    """An abstract class all 'hittable' objects inherit from
    """
    def hit(self, pt, dr, r_t : Interval, hit_record : HitRecord) -> bool:
        raise NotImplementedError
    
class HittableList(Hittable):
    """A class that collects all Hittable objects in a list
    """
    def __init__(self):
        self.obs = []
    
    def add(self, hob : Hittable) -> None:
        """Adds a Hittable object to the list.
        """
        self.obs.append(hob)
    
    def hit(self,
            pt,
            dr,
            r_t : Interval,
            rec : HitRecord) -> bool:
        """Iterates through the Hittable objects and looks for the closest 
        object hit by the ray. Returns True if an object is hit, and False
        otherwise.

        The method will also pass the hit information to the given rec.
        """
        temp_rec : HitRecord = HitRecord()
        hit_any: bool = False
        nearest = r_t.max

        for hob in self.obs:
            if hob.hit(pt, dr, Interval(r_t.min, nearest), temp_rec):
                hit_any = True
                nearest = temp_rec.t
                
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t
                rec.front_face = temp_rec.front_face
                rec.mat = temp_rec.mat
        
        return hit_any


# Geometries

class Sphere(Hittable):
    """A class that represents a sphere geometry.
    """
    def __init__(self, center, radius : float, mat) -> None:
        self.__center = center
        self.__radius = radius
        self.__mat = mat

    def hit(self, pt, dr, i : Interval, hrec : HitRecord) -> bool:
        """Returns True if the sphere is hit by the ray, and False otherwise.
        The method will also pass the hit information to the given rec.
        """
        q = pt
        d = dr

        a = d.dot(d)
        x = self.__center - q
        h = d.dot(x)
        c = x.dot(x) - self.__radius*self.__radius

        discriminant = h*h - a*c
        
        if discriminant < 0: 
            return False
        
        sqrt_result = np.sqrt(discriminant)

        t1 = (h - sqrt_result) / a
        t2 = (h + sqrt_result) / a
        
        t = None
        if i.contains(t2):
            t = t2
        
        # take negative since 'forward' is -z
        if i.contains(t1):
            t = t1
        
        if t is None:
            return False
        
        hrec.t = t
        hrec.p = pt + dr*t
        outward_normal = (hrec.p - self.__center) / self.__radius
        hrec.set_face_normal(pt, dr, outward_normal)
        hrec.mat = self.__mat

        return True