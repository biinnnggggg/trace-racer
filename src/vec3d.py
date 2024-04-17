import numpy as np

from .tracer_utility import *

class Vec3D:
    """Wrapper class for a numpy array.
    """
    def __init__(self,
                 x : float,
                 y : float,
                 z : float) -> None:
        self.vec = np.array([x, y, z])
    
    @classmethod
    def copy(cls, other : 'Vec3D') -> 'Vec3D':
        assert np.shape(other.vec) == (3,)
        return Vec3D(other.vec[0], other.vec[1], other.vec[2])

    @classmethod
    def of(cls, vec) -> 'Vec3D':
        assert np.shape(vec) == (3,)
        return Vec3D(vec[0], vec[1], vec[2])
    
    @classmethod
    def zero(cls) -> 'Vec3D':
        return Vec3D(0.0, 0.0, 0.0)
    
    @classmethod
    def rand(cls) -> 'Vec3D':
        return Vec3D(rand_float(), rand_float(), rand_float())
    
    @classmethod
    def rand_in(cls, a : float, b : float) -> 'Vec3D':
        return Vec3D( \
            rand_float_in(a, b), rand_float_in(a, b), rand_float_in(a, b))
    
    @classmethod
    def rand_in_unit_sphere(cls) -> 'Vec3D':
        while True:
            p = cls.rand()
            if p.length() < 1: return p

    @classmethod
    def rand_unit_vector(cls) -> 'Vec3D':
        return cls.get_unit_vector(cls.rand_in_unit_sphere())
    
    @classmethod
    def rand_on_hemisphere(cls, normal : 'Vec3D') -> 'Vec3D':
        p = cls.rand_in_unit_sphere()
        if p.dot(normal) >= 0.0: return p
        return -p

    # getters
    def get_x(self) -> float:
        return self.vec[0]

    def get_y(self) -> float:
        return self.vec[1]
    
    def get_z(self) -> float:
        return self.vec[2]

    # utility methods
    def __neg__(self) -> 'Vec3D':
        return Vec3D.of(-self.vec)
    
    def __getitem__(self, key : int) -> float:
        return self.vec[key]
    
    def __iadd__(self, other : 'Vec3D') -> 'Vec3D':
        self.vec += other.vec
        return self

    def __imul__(self, scalar : float) -> 'Vec3D':
        self.vec *= scalar
        return self
    
    def __itruediv__(self, scalar : float) -> 'Vec3D':
        self.vec /= scalar
        return self
    
    def length(self) -> float:
        return np.linalg.norm(self.vec)
    
    def length_squared(self) -> float:
        return self.vec.dot(self.vec)
    
    # more utility
    def __str__(self) -> str:
        return f'{self.vec[0]} {self.vec[1]} {self.vec[2]}'

    def __add__(self, other : 'Vec3D') -> 'Vec3D':
        return Vec3D.of(self.vec + other.vec)
    
    def __sub__(self, other : 'Vec3D') -> 'Vec3D':
        return Vec3D.of(self.vec - other.vec)

    def __mul__(self, scalar : float) -> 'Vec3D':
        return Vec3D.of(self.vec * scalar)

    def __truediv__(self, scalar : float) -> 'Vec3D':
        return Vec3D.of(self.vec / scalar)

    def dot(self, other : 'Vec3D') -> float:
        return self.vec.dot(other.vec)
    
    def cross(self, other : 'Vec3D') -> 'Vec3D':
        return Vec3D.of(np.cross(self.vec, other.vec))

    @classmethod
    def get_unit_vector(cls, u : 'Vec3D') -> 'Vec3D':
        return Vec3D.of(u.vec / u.length())
    
    # even more utility
    def __eq__(self, other : 'Vec3D') -> bool:
        return np.allclose(self.vec, other.vec) 


Point3D = Vec3D
