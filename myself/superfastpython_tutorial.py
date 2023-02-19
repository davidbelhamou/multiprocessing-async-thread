from datetime import datetime
from time import sleep
from multiprocessing import Process
import pandas as pd


# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('This is from another process')
