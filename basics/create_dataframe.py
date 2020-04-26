#!/usr/bin/env python3
"""
Examples on creating data frames.
  . Load from files.
  . Create from arrays.

Reference:
  . https://scipy-lectures.org/packages/statistics/index.html
  . https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url

"""

import logging
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

BRAIN_SIZE_PATH = "../data/brain_size.csv"
BRAIN_SIZE_URL = "https://raw.githubusercontent.com/cogmaster-stats/python-cogstats/master/examples/brain_size.csv"


def load_brain_size(path):
    """ Load brain_size.csv """
    df = pd.read_csv(path, sep=';', na_values='.', index_col=0)
    logger.info("Data Frame:\n{}".format(df.head()))
    return df


def load_brain_size_csv_file():
    """ Load a local CSV file. """
    path = BRAIN_SIZE_PATH
    logger.info("Loading {}...".format(path))
    return load_brain_size(path)


def load_brain_size_csv_url():
    """ Starting Pandas 0.19.2, you read_csv can take an URL as the path. """
    path = BRAIN_SIZE_URL
    logger.info("Loading {}...".format(path))
    return load_brain_size(path)


def create_sin_cos_dataframe():
    """ Create a dataframe from arrays. """
    t = np.linspace(-6, 6, 20)
    sin_t = np.sin(t)
    cos_t = np.sin(t)
    #logger.debug("- t: {}".format(t))
    #logger.debug("- sin: {}".format(sin_t))
    #logger.debug("- cos: {}".format(cos_t))
    df = pd.DataFrame({'t':t, 'sin':sin_t, 'cos':cos_t})
    logger.info("Data Frame:\n{}".format(df.head()))

    logger.info("- shape = {}".format(df.shape))
    logger.info("- columns = {}".format(df.columns))

    return df


# ----------------
#   Main
# ----------------
def init_logging():
    """ Initialize logging. """
    fmt = "%(asctime)s %(levelname)s [%(funcName)s] %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.DEBUG)


def main():
    """ Main function. """
    # Logging
    init_logging()

    # Tests
    load_brain_size_csv_file()
    load_brain_size_csv_url()
    create_sin_cos_dataframe()


if __name__ == "__main__":
    main()
