import logging

logger = logging.getLogger(__name__)

def create_logger():
    logging.basicConfig(filename='main.log', level=logging.INFO)

if __name__ == '__main__':

    create_logger()
    logger.info('Started')

    # Image
    image_width : int = 256
    image_height : int = 256

    # Render
    print('P3')
    print(f'{image_width} {image_height}')
    print('255')
    
    for j in range(image_height):
        logger.info(f'\rScanlines remaining: {image_height - j}')
        for i in range(image_width):
            # Values from 0.0 to 1.0
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0.0

            # Scaled to 0 to 255
            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f'{ir} {ig} {ib}')
    

    logger.info('Finished')