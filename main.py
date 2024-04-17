import time

from src.tracer_utility import *
from src.hittable import *
from src.camera import *

if __name__ == '__main__':

    # Create world
    world = HittableList()
    world.add(Sphere(Point3D(0.0, 0.0, -1.0), 0.5))
    world.add(Sphere(Point3D(0, -100.5, -1), 100))

    logger = Output('log')

    Camera.aspect_ratio = 16 / 9
    Camera.image_width = 400
    Camera.samples_per_pixel = 20

    output_filepath = 'data/output.png'

    start = time.time()

    view = Camera.render(world)
    view.save(output_filepath)
    
    end = time.time()

    logger.write(end - start)
