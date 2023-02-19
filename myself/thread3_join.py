import threading
import logging
import time

'''
    Create a TTL
'''

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s %(message)s]')


def f(name):
    logging.info(f'f() started with name {name}')
    time.sleep(5)
    logging.info(f'f() ended')


if __name__ == '__main__':
    logging.info(f'main started')
    t = threading.Thread(target=f, args=['david'], daemon=True)
    t.start()
    time.sleep(4)
    logging.info(f'thread is alive: {t.is_alive()}')
    logging.info('main ended')
