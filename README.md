# trace-racer

A toy ray-tracer written in Python. The implementation loosely follows the
[Ray Tracing in One Weekend](https://raytracing.github.io/books/RayTracingInOneWeekend.html) series.

Below is an image of the latest render from the code:

This image took 2.5 hr to render. Given that the resolution isn't very high, and
the sampling level is quite low, this performance is disappointing but expected.
![Latest Render](data/final-render.png)

## Quick start

1. Ensure that you have Python 3.11 or above installed on your computer.
2. Clone the repo and install any necessary dependencies by running these commands in the terminal:

```bash
git clone https://github.com/biinnnggggg/trace-racer.git

pip install numpy, PIL
```

3. Describe world to render in `main.py` and run the file.

```py
if __name__ == '__main__':
    #...
    # Create world
    world = HittableList()

    # Materials
    material_ground = Lambertian(np.array([0.8, 0.8, 0.35]))
    material_blue = Lambertian(np.array([0.1, 0.2, 0.5]))
    material_powderblue = Lambertian(np.array([0.7, 0.9, 0.92]))
    #... add materials here...

    # Objects
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
        Sphere(np.array([-1.25, 0.0, 0.5]), 0.5, material_red),\
        # ... add objects here
    ]

    # Add objects to world
    for sphere in spheres:
        world.add(sphere)

    # Logger?
    logger = Output('log')

    # Change camera settings here...
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
    ...

```

4. The render output should be saved as `data/output.png`.
5. The render log should be saved as `main.log`

## Upcoming features

1. ~~Positionable camera~~
2. ~~Blur~~, ~~field of view~~, ~~depth of field,...~~
3. Textures
4. More unit tests, and preliminary integration testing
5. Cubes and polyhedrons
6. Description language

### Resources I used along the way:

- https://docs.python-guide.org/writing/structure/
- https://docs.python-guide.org/writing/tests/
- https://docs.python.org/3/library/logging.html
- https://stackoverflow.com/questions/33189208/vs-for-a-power-of-2-operation
- https://www.youtube.com/watch?v=TrqK-atFfWY - different ways of optimising
ray tracers e.g. bounding volume, BVH, ...
- https://angms.science/doc/RM/randUnitVec.pdf - how to generate uniform unit
vectors in Rn efficiently using normal distribution sampling.