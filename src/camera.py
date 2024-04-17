from .tracer_utility import *
from .hittable import *

log = Output('log')
stdout = Output('stdout')

class Camera:
    """Defines the image dimensions and viewport.
    """

    # public fields
    aspect_ratio : float = 1.0   # ratio of image width over height
    image_width : int = 100      # rendered image width in pixel count
    samples_per_pixel : int = 10 # count of random samples for each pixel

    # private fields
    __image_height : int = None
    __pixel_samples_scale : float = None
    __center : Point3D = None
    __pixel00_loc : Point3D = None
    __pixel_delta_u : Vec3D = None
    __pixel_delta_v : Vec3D = None

    @classmethod
    def render(cls, world : Hittable) -> None:
        cls.__initialize()

        # Render
        stdout.write('P3')
        stdout.write(f'{cls.image_width} {cls.__image_height}')
        stdout.write('255')
        
        for j in range(cls.__image_height):
            # log.write(f'\rScanlines remaining: {image_height - j}')
            for i in range(cls.image_width):
                pixel_color = Color(0.0, 0.0, 0.0)
                for sample in range(cls.samples_per_pixel):
                    r = cls.__get_ray(i, j)
                    pixel_color += cls.__ray_color(r,world)

                write_color(stdout, pixel_color * cls.__pixel_samples_scale)

        # log.write('\rDone.')
    
    @classmethod
    def __initialize(cls) -> None:
        # Calculate the image height
        cls.__image_height : int = int(cls.image_width / cls.aspect_ratio)
        cls.__image_height = max(1, cls.__image_height)

        cls.__pixel_samples_scale = 1.0 / cls.samples_per_pixel

        # Camera
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * cls.image_width / cls.__image_height
        cls.__center = Point3D(0.0, 0.0, 0.0)

        # Calculate the viewport vectors
        viewport_u = Vec3D(viewport_width, 0, 0)
        viewport_v = Vec3D(0, -viewport_height, 0)

        cls.__pixel_delta_u = viewport_u / cls.image_width
        cls.__pixel_delta_v = viewport_v / cls.__image_height

        # Calculate the location of the left upper pixel
        viewport_upper_left = cls.__center - Vec3D(0, 0, focal_length) \
            - viewport_u / 2 - viewport_v / 2
        
        cls.__pixel00_loc = viewport_upper_left \
            + (cls.__pixel_delta_u + cls.__pixel_delta_v) * 0.5
    
    @classmethod
    def __get_ray(cls, i : int, j : int) -> Ray:
        """Constructs a camera ray originating from the origin and directed at
        randomly points around the pixel location (i, j)
        """

        offset = cls.__sample_square()
        pixel_sample = cls.__pixel00_loc \
              + cls.__pixel_delta_u * (i + offset.get_x()) \
              + cls.__pixel_delta_v * (j + offset.get_y())
        
        r_origin = cls.__center
        r_dir = pixel_sample - r_origin

        return Ray(r_origin, r_dir)
        
    
    @classmethod
    def __ray_color(cls, r : Ray, world : HittableList) -> Color:
        if world.hit(r, Interval(0, INF), hit_record := HitRecord()):
            n : Vec3D = hit_record.normal
            color : Color = (n + Color(1, 1, 1)) * 0.5
            return color

        # sky -> linear interpolation from blue to white
        unit_dir : Vec3D = Vec3D.get_unit_vector(r.get_direction())
        a = 0.5 * (unit_dir.get_y() + 1.0)
        start_value : Color = Color(1.0, 1.0, 1.0) # white
        end_value : Color = Color(0.5, 0.7, 1.0) # blue 
        color : Color = start_value * (1 - a) + end_value * a
        return color

    # helper functions

    @classmethod
    def __sample_square(cls) -> Point3D:
        """Returns a random sample point within the unit square centred at the
        origin.
        """
        rand_x : float = rand_float_in(-0.5, 0.5)
        rand_y : float = rand_float_in(-0.5, 0.5)
        return Point3D(rand_x, rand_y, 0.0)