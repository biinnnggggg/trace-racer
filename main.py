import time

from src.tracer_utility import *
from src.hittable import *
from src.camera import *
from src.output import Output

if __name__ == '__main__':

    # Create world
    world = HittableList()
    world.add(Sphere(np.array([0.0, 0.0, -1.0]), 0.5))
    # world.add(Sphere(np.array([2.0, 0.0, -3.0]), 0.5))
    # world.add(Sphere(np.array([0.0, 0.0, -0.5]), 0.3))
    world.add(Sphere(np.array([0.0, -100.5, -1.0]), 100))

    logger = Output('log')

    Camera.aspect_ratio = 16 / 9
    Camera.image_width = 400
    Camera.samples_per_pixel = 100
    Camera.max_depth = 50

    output_filepath = 'data/output.png'

    start = time.time()

    view = Camera.render(world)
    view.save(output_filepath)
    
    end = time.time()

    logger.write(end - start)
