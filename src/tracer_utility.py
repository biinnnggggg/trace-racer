import numpy as np 

# Constants
INF : float = 10e12
PI : float = 3.1415926535897932385

RNG = np.random.default_rng()
epsilon = 1e-8

# Utility functions

def deg_to_rad(degrees : float) -> float:
    """Converts an angle from degrees to radians.
    """
    return degrees * PI / 180.0

def rand_in_unit_sphere():
        while True:
            p = RNG.random(3)
            if np.linalg.norm(p) < 1: return p

def rand_unit_vector():
        vec = rand_in_unit_sphere()
        return get_unit_vector(vec)

def is_near_zero(vec) -> bool:
      return vec[0] < epsilon and vec[1] < epsilon and vec[2] < epsilon
    
def get_unit_vector(vec):
      return vec / np.linalg.norm(vec)

def get_reflection(vec, normal):
      return vec - 2 * vec.dot(normal)*normal

def get_refraction(vec, normal, ref_index_ratio):
      cos_theta = min(-vec.dot(normal), 1.0)
      ref_vec_perp = ref_index_ratio * (vec + cos_theta*normal)
      length = np.linalg.norm(ref_vec_perp)
      ref_vec_para = -np.sqrt(1.0 - length*length) * normal
      return ref_vec_perp + ref_vec_para