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

    start = time.time()
    Camera.render(world)
    end = time.time()

    logger.write(end - start)
