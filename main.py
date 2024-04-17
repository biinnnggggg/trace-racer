from src.tracer_utility import *
from src.hittable import *
from src.output import *

log = Output('log')
stdout = Output('stdout')

def ray_color(ray : Ray, world : HittableList) -> Color:
    if world.hit(ray, Interval(0, INF), hit_record := HitRecord()):
        n : Vec3D = hit_record.normal
        color : Color = (n + Color(1, 1, 1)) * 0.5
        return color

    # sky -> linear interpolation from blue to white
    unit_dir : Vec3D = Vec3D.get_unit_vector(ray.get_direction())
    a = 0.5 * (unit_dir.get_y() + 1.0)
    start_value : Color = Color(1.0, 1.0, 1.0) # white
    end_value : Color = Color(0.5, 0.7, 1.0) # blue 
    color : Color = start_value * (1 - a) + end_value * a
    return color

if __name__ == '__main__':

    # Image
    aspect_ratio = 16.0 / 9.0
    image_width : int = 256

    # Calculate the image height
    image_height : int = int(image_width / aspect_ratio)
    image_height = max(1, image_height)

    # Create world
    world = HittableList()
    world.add(Sphere(Point3D(0.0, 0.0, -1.0), 0.5))
    world.add(Sphere(Point3D(0, -100.5, -1), 100))

    # Camera
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * image_width / image_height
    camera_center = Point3D(0.0, 0.0, 0.0)

    # Calculate the viewport vectors
    viewport_u = Vec3D(viewport_width, 0, 0)
    viewport_v = Vec3D(0, -viewport_height, 0)

    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    # Calculate the location of the left upper pixel
    viewport_upper_left = camera_center - Vec3D(0, 0, focal_length) \
         - viewport_u / 2 - viewport_v / 2
    pixel00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5


    # Render
    print('P3')
    print(f'{image_width} {image_height}')
    print('255')
    
    for j in range(image_height):
        # log.write(f'\rScanlines remaining: {image_height - j}')
        for i in range(image_width):
            pixel_center = pixel00_loc + pixel_delta_u * i + pixel_delta_v * j
            ray_dir = pixel_center - camera_center
            r = Ray(camera_center, ray_dir)

            pixel_color = ray_color(r, world)
            write_color(stdout, pixel_color)

    # log.write('\rDone.')