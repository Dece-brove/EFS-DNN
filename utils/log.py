import csv
import os
from pathlib import Path
import logging
import time


def set_logger(dataset, classes, num_in_feat, n_lgb, r_sample):
    task_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    Path("log/").mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(f'log/{dataset}_{classes}_{num_in_feat}_{n_lgb}_{r_sample}_{task_time}.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
