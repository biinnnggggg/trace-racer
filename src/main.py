from .color import *
from .output import *
from .vec3d import *

log = Output('log')
stdout = Output('stdout')

if __name__ == '__main__':

    # Image
    image_width : int = 256
    image_height : int = 256

    # Render
    print('P3')
    print(f'{image_width} {image_height}')
    print('255')
    
    for j in range(image_height):
        log.write(f'\rScanlines remaining: {image_height - j}')
        for i in range(image_width):
            pixel_color = Color(np.array([i/(image_width-1), j/(image_height-1), 0]))
            write_color(stdout, pixel_color)

    log.write('\rDone.')