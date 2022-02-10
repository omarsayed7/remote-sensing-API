from skimage.io import imread
import time
import cv2
from skimage import feature
from skimage.color import label2rgb
from skimage.io import imread
import mahotas as mt
import json
import numpy as np
import os
import progressbar
from numpy.lib import stride_tricks

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pickle

img_data1 = imread('img-4-7.jpg')
