import time

from src.tracer_utility import *
from src.hittable import *
from src.camera import *
from src.material import *
from src.output import Output

if __name__ == '__main__':

    # Create world
    world = HittableList()

    material_ground = Lambertian(np.array([0.8, 0.8, 0.35]))
    material_blue = Lambertian(np.array([0.1, 0.2, 0.5]))
    material_powderblue = Lambertian(np.array([0.7, 0.9, 0.92]))
    material_red = Lambertian(np.array([1.0, 0.5, 0.3]))
    material_purple = Lambertian(np.array([0.75, 0.45, 0.75]))
    material_yellow = Lambertian(np.array([0.95, 0.95, 0.05]))
    material_glass = Dielectric(1.50)
    material_bubble = Dielectric(1 / 1.50)
    material_reflectless = Metal(np.array([0.8, 0.6, 0.2]), 0.1)
    material_reflect = Metal(np.array([0.8, 0.9, 0.8]), 0.04)

    spheres = [
        Sphere(np.array([0.0, -100.5, -1.0]), 100.0, material_ground),
        Sphere(np.array([0.0, 0.0, -1.2]), 0.5, material_powderblue),
        Sphere(np.array([4.8, 0.0, 1.2]), 0.5, material_powderblue),
        Sphere(np.array([-1.0, 0.0, -1.0]), 0.5, material_glass),
        Sphere(np.array([-1.0, 0.0, -1.0]), 0.45, material_bubble),
        Sphere(np.array([1.4, 0.0, -0.8]), 0.5, material_glass),
        Sphere(np.array([1.4, 0.0, -0.8]), 0.45, material_bubble),        
        Sphere(np.array([0.75, 0.0, 0.75]), 1, material_reflectless),
        Sphere(np.array([-3.5, 1.3, -0.8]), 1.75, material_reflect),
        Sphere(np.array([-0.5, 0.0, -3.0]), 0.5, material_red),
        Sphere(np.array([-1.25, 0.0, 0.5]), 0.5, material_red),
        Sphere(np.array([-1.0, 0.4, 1.6]), 0.7, material_purple),
        Sphere(np.array([6.25, 0.2, -1.3]), 0.7, material_yellow)   
    ]

    for sphere in spheres:
        world.add(sphere)

    logger = Output('log')

    # Camera
    Camera.aspect_ratio = 16 / 9 
    Camera.image_width = 720
    Camera.samples_per_pixel = 100
    Camera.max_depth = 30

    Camera.vfov = 100
    Camera.look_from = np.array([-2.0, 2.0, 1.0])
    Camera.look_at   = np.array([0.0, 0.0, -1.0])
    Camera.vup       = np.array([0.0, 1.0, 0.0])

    Camera.defocus_angle = 3.0
    Camera.focus_dist = 3.4

    output_filepath = 'data/output.png'

    start = time.time()

    view = Camera.render(world)
    view.save(output_filepath)
    
    end = time.time()

    logger.write(end - start)
