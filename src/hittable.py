from .tracer_utility import *

class HitRecord:
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
    def hit(self, r : Ray, t_min : float, t_max : float, hit_record : HitRecord) -> bool:
        raise NotImplementedError
    
class HittableList(Hittable):
    def __init__(self):
        self.obs = []
    
    def add(self, hob : Hittable) -> None:
        self.obs.add(hob)
    
    def hit(self,
            r : Ray,
            t_min : float,
            t_max : float,
            rec : HitRecord) -> bool:
        temp_rec : HitRecord = HitRecord()
        hit_any : bool
        nearest = t_max

        for hob in self.obs:
            if hob.hit(r, t_min, nearest, temp_rec):
                hit_any = True
                nearest = temp_rec.t
                
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t
                rec.front_face = temp_rec.front_face
        
        return hit_any


# Geometries

class Sphere(Hittable):
    def __init__(self, center : Point3D, radius : float) -> None:
        self.__center = center
        self.__radius = radius

    def hit(self, r : Ray, t_min : float, t_max : float, rec : HitRecord) -> bool:
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
        if t_min <= t2 <= t_max:
            t = t2
        
        # take negative since 'forward' is -z
        if t_min <= t1 <= t_max:
            t = t1
        
        if t is None:
            return False
        
        rec.t = t
        rec.p = r.at(t)
        outward_normal = (rec.p - self.__center) / self.__radius
        rec.set_face_normal(r, outward_normal)        

        return True