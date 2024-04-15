import logging

class Output:
    modes = ['stdout', 'log']
    logger_filename = '../main.log'

    logger = logging.getLogger()
    logging.basicConfig(filename=logger_filename, level=logging.INFO)

    def __init__(self, mode='stdout') -> None:
        if mode not in self.modes:
            raise ValueError(f'Invalid mode: {mode}. Please choose from {self.modes}.')
        self.mode = mode            
    
    def write(self, string : str) -> None:
        if self.mode == 'stdout':
            print(string)
        elif self.mode == 'log':
            self.logger.info(string)
