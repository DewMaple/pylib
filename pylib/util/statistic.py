# coding=utf-8
"""
Created on 2016年10月8日

@author: dengdan
"""
import numpy as np

from pylib import util


def D(x):
    x = util.np.flatten(x)
    return np.var(x)


def E(x):
    x = util.np.flatten(x)
    return np.average(x)
