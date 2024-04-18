from .tracer_utility import *
from .hittable import HitRecord

class Material:
    def scatter(pt, dr, hrec : HitRecord, attenuation,
                scattered_pt, scattered_dr) -> bool:
        return False