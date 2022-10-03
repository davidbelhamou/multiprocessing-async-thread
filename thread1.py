import threading
import logging
import time

'''
    Create a simple thread and see who finish first between the main thread and the thread t
'''

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s %(message)s]')


def f(name):
    logging.info(f'f() started with name {name}')
    time.sleep(5)
    logging.info(f'f() ended')


if __name__ == '__main__':
    logging.info(f'main started')
    t = threading.Thread(target=f, args=['david'])
    t.start()
    logging.info('main ended')


