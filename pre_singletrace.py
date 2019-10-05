# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:15:35 2018

@author: TX
"""

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.utils import plot_model
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio 
#numpy.random.seed(7)
import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"

matfn='predata_cnn.mat'
data=sio.loadmat(matfn)
x_pre=data['predata_cnn']
img_rows, img_cols = 1, 701
x_pre = x_pre.reshape(x_pre.shape[0], img_cols, 1)

model = load_model('single_polarity.cnn') 
 
#verbose:训练时显示实时信息，0表示不显示数据，1表示显示进度条，2表示用只显示一个数�?
classes=model.predict(x_pre,batch_size=8,verbose=0)
#np.savetxt("predict_singletrace1.txt", classes)
np.savetxt("predict_singletrace2.txt", classes)

'''
y_pre0= []
for i in range(classes.shape[0]):
    if classes[i,1]>0.8:
#        print(classes[i,0])
        y_pre0.append(1)
    elif classes[i,2]>0.8:
        y_pre0.append(2)
    else:
        y_pre0.append(0)   
    
plt.figure()
plt.plot(y_pre-y_pre0,'b',label='True')
#plt.plot(y_pre0,'r', linestyle='-.', label='CNN')

y_pre1=np.array(y_pre0)
np.savetxt("predict_result1.txt", y_pre1)
np.savetxt("true_result1.txt", y_pre)

'''

