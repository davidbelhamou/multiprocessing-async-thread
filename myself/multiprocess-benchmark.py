import collections
import multiprocessing
import logging
import time
from collections import namedtuple
import os
from tqdm import tqdm

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s %(message)s]')

scientists = [{"name": 'david', "age": 1991},
              {"name": 'elysa', "age": 1995},
              {"name": 'sam', "age": 1989},
              {"name": 'kim', "age": 1990},
              {"name": 'dima', "age": 1988},
              {"name": 'elad', "age": 1987},
              {"name": 'nir', "age": 1986}]


def transform(x):
    # print(f'Process {os.getpid()} Processing record {x["name"]}')
    time.sleep(1)
    res = {'name': x["name"], 'age': 2022 - x['age']}
    # print(f'Done processing record {x["name"]}')
    return res


def process_async(func, args, num_executor, process_type='spawn'):
    ctx = multiprocessing.get_context(process_type)
    with ctx.Pool(processes=num_executor) as pool:
        res = [pool.apply_async(func, (arg,)) for arg in args]
        results = []
        for r in tqdm(res):
            results.append(r.get())

    return results


def process_multi(func_, iterable_, num_executor=3, max_tasks_child=1, run_type='map'):
    results = None
    pool = multiprocessing.Pool(processes=num_executor, maxtasksperchild=max_tasks_child)
    if run_type == 'map_async':
        results = [i for i in tqdm(pool.map_async(func_, iterable_).get())]
    elif run_type == 'map':
        results = list(tqdm(pool.map(func_, iterable_), total=len(iterable_)))
    elif run_type == 'imap_unordered':
        results = list(tqdm(pool.imap_unordered(func_, iterable_), total=len(iterable_)))
    elif run_type == 'imap':
        results = list(tqdm(pool.imap(func_, iterable_), total=len(iterable_)))
    # star map are not in use right now
    elif run_type == 'startmap':
        results = list(tqdm(pool.starmap(func_, iterable_), total=len(iterable_)))
    elif run_type == 'starmap_async':
        results = list(tqdm(pool.starmap_async(func_, iterable_), total=len(iterable_)))
    else:
        pass
    return results


def start_task(func, *args):
    start = time.time()
    res = func(*args)
    end = time.time()
    return res, (end - start)


if __name__ == '__main__':
    res_async, perf_async = start_task(process_async, transform, scientists, 5)
    res_multi_map, perf_multi_map = start_task(process_multi, transform, scientists, 5, 4)
    res_multi_map_async, perf_multi_map_async = start_task(process_multi, transform, scientists, 5, 4, 'map_async')
    res_multi_imap_unordered, perf_multi_imap_unordered = start_task(process_multi, transform, scientists, 5, 4, 'imap_unordered')
    res_multi_imap, perf_multi_imap = start_task(process_multi, transform, scientists, 5, 4, 'imap')

    print(
        f'\nTime to complete:\n task 1: {perf_async:.3f},'
        f' task 2: {perf_multi_map:.3f},'
        f' task 3: {perf_multi_map_async:.3f},'
        f' task 4: {perf_multi_imap_unordered:.3f},'
        f'task 5: {perf_multi_imap:.3f},')

    print(f'task1: {res_async}\n,'
          f'task2: {res_multi_map}\n,'
          f'task3: {res_multi_map_async}\n,'
          f'task4: {res_multi_imap_unordered}\n,'
          f'task4: {res_multi_imap}\n,')
