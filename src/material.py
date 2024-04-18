from .tracer_utility import *
from .hittable import HitRecord

class Material:
    def scatter(self, ray_pt, ray_dr, hrec : HitRecord) -> bool:
        return False, None, None, None
    

class Lambertian(Material):
    def __init__(self, albedo):
        self.__albedo = albedo
    
    def scatter(self, ray_pt, ray_dr, hrec : HitRecord):
        scatter_ray_dr = hrec.normal + rand_unit_vector()

        if is_near_zero(scatter_ray_dr):
            scatter_ray_dr = hrec.normal

        scatter_ray_pt = hrec.p
        attenuation = self.__albedo
        return True, scatter_ray_pt, scatter_ray_dr, attenuation


class Metal(Material):
    def __init__(self, albedo, fuzz):
        self.__albedo = albedo
        self.__fuzz = fuzz if fuzz < 1 else 1
    
    def scatter(self, ray_pt, ray_dr, hrec : HitRecord):
        reflected = get_reflection(ray_dr, hrec.normal)
        scatter_ray_dr = get_unit_vector(reflected) + self.__fuzz * rand_unit_vector() 
        scatter_ray_pt = hrec.p
        attenuation = self.__albedo
        scatter = (scatter_ray_dr.dot(hrec.normal) > 0)
        return scatter, scatter_ray_pt, scatter_ray_dr, attenuation

    
class Dielectric(Material):
    def __init__(self, ref_index):
        self.__ref_index = ref_index
    
    def scatter(self, ray_pt, ray_dr, hrec : HitRecord):
        attenuation = np.array([1.0, 1.0, 1.0])

        # take the refractive index of air to be 1
        ri = 1.0 / self.__ref_index if hrec.front_face else self.__ref_index

        unit_dr = get_unit_vector(ray_dr)

        # check for total internal reflection
        cos_theta = min(-unit_dr.dot(hrec.normal), 1.0)
        sin_theta = np.sqrt(1.0 - cos_theta*cos_theta)

        cannot_refract = ri * sin_theta > 1.0

        if (cannot_refract or self.reflectance(cos_theta, ri) > RNG.random()):
            reflected = get_reflection(unit_dr, hrec.normal)
            scatter_ray_dr = reflected
        else:
            refracted = get_refraction(unit_dr, hrec.normal, ri)
            scatter_ray_dr = refracted
        
        scatter_ray_pt = hrec.p
        
        return True, scatter_ray_pt, scatter_ray_dr, attenuation
    

    def reflectance(self, cos, ri):
        r0 = (1 - ri) / (1 + ri)
        r0 = r0*r0
        return r0 + (1 - r0)*pow((1 - cos), 5)