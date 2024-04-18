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

    