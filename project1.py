import logging

logging.basicConfig(filename='projec1.log', level=logging.ERROR, format = '%(levelname)s - %(asctime)s - %(message)s')

def add(x,y):
    try:
        logging.info('Project 1 started')
        logging.info(f'adding {x} and {y}')
        result = x+y
        logging.info(f'Result is {result}')
        logging.info('Project1 completed')
    except Exception as e:
        logging.error(e)



add(10,5)


add(5,'hello')
