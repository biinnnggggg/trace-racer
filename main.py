import time

from src.tracer_utility import *
from src.hittable import *
from src.camera import *
from src.material import *
from src.output import Output

if __name__ == '__main__':

    # Create world
    world = HittableList()

    material_ground = Lambertian(np.array([0.8, 0.8, 0.0]))
    material_center = Lambertian(np.array([0.1, 0.2, 0.5]))
    material_left = Dielectric(1.50)
    material_bubble = Dielectric(1 / 1.50)
    material_right = Metal(np.array([0.8, 0.6, 0.2]), 0.9)

    spheres = [
        Sphere(np.array([0.0, -100.5, -1.0]), 100.0, material_ground),
        Sphere(np.array([0.0, 0.0, -1.2]), 0.5, material_center),
        Sphere(np.array([-1.0, 0.0, -1.0]), 0.5, material_left),
        Sphere(np.array([-1.0, 0.0, -1.0]), 0.45, material_bubble),
        Sphere(np.array([1.0, 0.0, -1.0]), 0.5, material_right)
    ]

    for sphere in spheres:
        world.add(sphere)

    logger = Output('log')

    # Camera
    Camera.aspect_ratio = 16 / 9
    Camera.image_width = 400
    Camera.samples_per_pixel = 30
    Camera.max_depth = 20

    output_filepath = 'data/output.png'

    start = time.time()

    view = Camera.render(world)
    view.save(output_filepath)
    
    end = time.time()

    logger.write(end - start)
