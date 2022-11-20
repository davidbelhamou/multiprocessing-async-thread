# import threading
# import logging
# import time
#
# '''
#     Create a simple thread and see who finish first between the main thread and the thread t
# '''
#
# logging.basicConfig(level=logging.INFO,
#                     format='[%(asctime)s %(message)s]')
#
#
# def f(name):
#     logging.info(f'f() started with name {name}')
#     time.sleep(5)
#     logging.info(f'f() ended')
#
#
# if __name__ == '__main__':
#     logging.info(f'main started')
#     t = threading.Thread(target=f, args=['david'])
#     t.start()
#     logging.info('main ended')
#
#
# import re
#
# test_str = '/david/path/date=202-09-02.csv'
#
# all = re.findall("[\d]{4}-[\d]{1,2}-[\d]{2}", test_str)
#
# for s in all:

# from datetime import datetime
# import pendulum
#
#
# import pytz
#
# zones = pytz.all_timezones
#
# tz = pendulum.timezone("Asia/Jerusalem")
#
# tmp_today = datetime.now()
# today = datetime(tmp_today.year, tmp_today.month, tmp_today.day)

import argparse
# import papermill
from pathlib import Path


path = 'Demo/Hello \world woo.ipynb'

try:

    p = argparse.ArgumentParser()

    p.add_argument('--path', type=str, required=True)

    args = p.parse_args()

    print(args.path)
except Exception as ex:
    x = 1