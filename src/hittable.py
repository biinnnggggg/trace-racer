from .tracer_utility import *
from .ray import Ray
from .vec3d import Point3D, Vec3D
from .interval import Interval

class HitRecord:
    """Records information about Ray and Hittable object intersection.
    """
    def __init__(self,
                 p : Point3D=None,
                 normal : Vec3D=None,
                 t : float=None,
                 front_face : bool = None) -> None:
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def set_face_normal(self, r : Ray, outward_normal : Vec3D) -> None:
        """Sets the hit record normal vector. Note that the parameter `outward_normal`
        is assumed to have unit length.
        """
        assert np.isclose(outward_normal.length(), 1.0)
        self.front_face = r.get_direction().dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable:
    """An abstract class all 'hittable' objects inherit from
    """
    def hit(self, r : Ray, r_t : Interval, hit_record : HitRecord) -> bool:
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
            r : Ray,
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
            if hob.hit(r, Interval(r_t.min, nearest), temp_rec):
                hit_any = True
                nearest = temp_rec.t
                
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t
                rec.front_face = temp_rec.front_face
        
        return hit_any


# Geometries

class Sphere(Hittable):
    """A class that represents a sphere geometry.
    """
    def __init__(self, center : Point3D, radius : float) -> None:
        self.__center = center
        self.__radius = radius

    def hit(self, r : Ray, i : Interval, rec : HitRecord) -> bool:
        """Returns True if the sphere is hit by the ray, and False otherwise.
        The method will also pass the hit information to the given rec.
        """
        q = r.get_origin()
        d = r.get_direction()

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
        if i.contains(t2):
            t = t2
        
        # take negative since 'forward' is -z
        if i.contains(t1):
            t = t1
        
        if t is None:
            return False
        
        rec.t = t
        rec.p = r.at(t)
        outward_normal = (rec.p - self.__center) / self.__radius
        rec.set_face_normal(r, outward_normal)        

        return True