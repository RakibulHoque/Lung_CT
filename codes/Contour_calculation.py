# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:51:45 2018

@author: DSP Research Lab
"""
import pydicom as dicom
import numpy as np
from scipy.sparse import csc_matrix
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import operator
import warnings
import glob

path = "G:\\VIP_CUP18_ValidationData\\VIP_CUP18_ValidationData\\"

if path[-1] != '\\': path += '\\'
# get all .dcm  file
fpaths = glob.glob(path + '*\\*\\*\\*.dcm')
#fpath = fpaths[4000]
i = 0
for fpath in fpaths:
    i = i + 1
    f = dicom.read_file(fpath)
    if 'ROIContourSequence' in dir(f):
        print("Ground Truth Present! \n Slice No:", i)
        
        break
    