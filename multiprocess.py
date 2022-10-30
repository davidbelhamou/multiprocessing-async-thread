import collections
import multiprocessing
import logging
import time
from collections import namedtuple
import os

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s %(message)s]')

scientists = [{"name": 'david', "age": 1991},
              {"name": 'elysa', "age": 1995},
              {"name": 'sam', "age": 1989},
              {"name": 'kim', "age": 1990}]


def transform(x):
    print(f'Process {os.getpid()} Processing record {x["name"]}')
    time.sleep(1)
    res = {'name': x["name"], 'age': 2022 - x['age']}
    print(f'Done processing record {x["name"]}')
    return res


if __name__ == '__main__':
    start = time.time()

    pool = multiprocessing.Pool(processes=3, maxtasksperchild=1)
    results = pool.map(transform, scientists)
    # results = tuple(map(transform, scientists))

    end = time.time()

    print(f'\nTime to complete {end - start:.2f}')
    print(results)
