from .tracer_utility import *
from .hittable import *

log = Output('log')
stdout = Output('stdout')

class Camera:
    """Defines the image dimensions and viewport.
    """

    # public fields
    aspect_ratio : float = 1.0
    image_width : int = 256

    # private fields
    __image_height : int = None
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
                pixel_center = cls.__pixel00_loc + cls.__pixel_delta_u * i \
                    + cls.__pixel_delta_v * j
                ray_dir = pixel_center - cls.__center
                r = Ray(cls.__center, ray_dir)

                pixel_color = cls.__ray_color(r,world)
                write_color(stdout, pixel_color)

        # log.write('\rDone.')
    
    @classmethod
    def __initialize(cls) -> None:
        # Calculate the image height
        cls.__image_height : int = int(cls.image_width / cls.aspect_ratio)
        cls.__image_height = max(1, cls.__image_height)

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
        cls.__pixel00_loc = viewport_upper_left + (cls.__pixel_delta_u + cls.__pixel_delta_v) * 0.5
    
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

        