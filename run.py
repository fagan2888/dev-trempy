#!/usr/bin/env python
import sys
import filecmp
sys.path.insert(0, "../../copulpy")
import copulpy

import numpy as np
import random

from trempy.clsModel import ModelCls
from trempy import estimate
from trempy import simulate
from trempy.tests.test_auxiliary import get_random_init, get_rmse
from trempy.read.read import read
import os
from trempy.paras.clsParas import ParasCls
import sys

np.random.seed(13)
#simulate('simulate.trempy.ini')
estimate('simulate.trempy.ini')
