# what is a generator?
# a generator is a sequence of variables like str, int etc...
# compare to a list or dict a generator implement the yield keyword
import time
from random import randint
import asyncio


def odds(s, e):
    for i in range(s, e + 1, 2):
        yield i


async def rand():
    await asyncio.sleep(3)
    return randint(1, 10)


async def square_odds(s, e):
    for odd in odds(s, e):
        await asyncio.sleep(1)
        yield odd ** 2


async def main(s, e):
    res = [odd for odd in odds(s, e)]
    print(res)

    start = time.perf_counter()
    r = await rand()
    elapse = time.perf_counter() - start
    print(f'r: {r}, took {elapse:.2f}s')

    start = time.perf_counter()
    r = await asyncio.gather(*(rand() for _ in range(10)))
    elapse = time.perf_counter() - start
    print(f'r: {r}, took {elapse:.2f}s')

    async for so in square_odds(11, 17):
        print("so: ", so)


if __name__ == '__main__':
    asyncio.run(main(2, 12))
