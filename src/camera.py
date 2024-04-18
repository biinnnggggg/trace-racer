from PIL import Image

from .tracer_utility import *
from .interval import Interval
from .hittable import HitRecord, Hittable, HittableList
from .color import process

class View:
    """Represents the camera view.
    """
    def __init__(self, width : int, height : int) -> None:
        self.image_array = [[None for _ in range(width)] for _ in range(height)]
    
    def paint(self, i : int, j : int, color) -> None:
        self.image_array[i][j] = process(color)
    
    def save(self, path : str) -> None:
        image = Image.fromarray(np.array(self.image_array, dtype=np.uint8))
        image.save(path)

class Camera:
    """Defines the image dimensions and viewport.
    """

    # public fields
    aspect_ratio : float = 1.0   # ratio of image width over height
    image_width : int = 100      # rendered image width in pixel count
    samples_per_pixel : int = 10 # count of random samples for each pixel
    max_depth : int = 5          # max number of ray bounces
    view : View = None
    

    # private fields
    __image_height : int = None
    __center = None
    __pixel00_loc = None
    __pixel_delta_u = None
    __pixel_delta_v = None

    @classmethod
    def render(cls, world : Hittable) -> View:
        cls.__initialize()
        
        for i in range(cls.__image_height):
            for j in range(cls.image_width):
                pixel_color = cls.__get_pixel_color(i, j, world)
                cls.view.paint(i, j, pixel_color)
        
        return cls.view
    
    @classmethod
    def __initialize(cls) -> None:
        # Calculate the image height
        cls.__image_height : int = int(cls.image_width / cls.aspect_ratio)
        cls.__image_height = max(1, cls.__image_height)

        cls.view = View(cls.image_width, cls.__image_height)

        # Camera
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * cls.image_width / cls.__image_height
        cls.__center = np.array([0.0, 0.0, 0.0])

        # Calculate the viewport vectors
        viewport_u = np.array([viewport_width, 0, 0])
        viewport_v = np.array([0, -viewport_height, 0])

        cls.__pixel_delta_u = viewport_u / cls.image_width
        cls.__pixel_delta_v = viewport_v / cls.__image_height

        # Calculate the location of the left upper pixel
        viewport_upper_left = cls.__center - np.array([0, 0, focal_length]) \
            - viewport_u / 2 - viewport_v / 2
        
        cls.__pixel00_loc = viewport_upper_left \
            + (cls.__pixel_delta_u + cls.__pixel_delta_v) * 0.5
    
    @classmethod
    def __ray_color(cls, ray_pt, ray_dr, depth : int, world : HittableList):
        black = np.array([0.0, 0.0, 0.0])

        if depth <= 0:
            return black

        if world.hit(ray_pt, ray_dr, Interval(0.001, INF), hrec := HitRecord()):
            scattered, scatter_ray_pt, scatter_ray_dr, attenuation = \
                hrec.mat.scatter(ray_pt, ray_dr, hrec)
            
            if scattered: return attenuation * cls.__ray_color(
                scatter_ray_pt,scatter_ray_dr, depth-1, world)
            return black
        
        # skybox -> linear interpolation from blue to white
        unit_dr = ray_dr / np.linalg.norm(ray_dr)
        a = 0.5 * (unit_dr[1] + 1.0)
        start_value = np.array([1.0, 1.0, 1.0]) # white
        end_value = np.array([0.5, 0.7, 1.0]) # blue 
        color = start_value * (1-a) + end_value * a
        return color

    @classmethod
    def __get_pixel_color(cls, i : int, j : int, world : HittableList):
        x, y = j, i

        # Generate all rays at once
        vec_shape = (cls.samples_per_pixel, 1)
        x_offsets = RNG.random(vec_shape) - np.full(vec_shape, 0.5)
        y_offsets = RNG.random(vec_shape) - np.full(vec_shape, 0.5)
        x_s = np.full(vec_shape, x) + x_offsets
        y_s = np.full(vec_shape, y) + y_offsets
        

        mat_shape = (cls.samples_per_pixel, 3)
        pixel_samples = np.tile(cls.__pixel00_loc.reshape(1, -1), cls.samples_per_pixel).reshape(mat_shape) \
                        + x_s * cls.__pixel_delta_u.reshape(1, -1)  \
                        + y_s * cls.__pixel_delta_v.reshape(1, -1)
        r_origins = np.tile(cls.__center.reshape(1, -1), cls.samples_per_pixel).reshape(mat_shape)
        r_dirs = pixel_samples - r_origins

        # Calculate colors for all rays
        res_arr = np.empty_like(r_origins)
        for i, (row1, row2) in enumerate(zip(r_origins, r_dirs)):
            res_arr[i] = cls.__ray_color(row1, row2, cls.max_depth, world)
        
        pixel_color = np.mean(res_arr, axis=0)
        
        return pixel_color