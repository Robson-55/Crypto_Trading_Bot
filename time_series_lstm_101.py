# -*- coding: utf-8 -*-
"""Time_series_LSTM_101.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e0z8K4b2SD9LQ7kNCRYW-V8Ae0_TvD6J
"""

# LSTM approach

# There ar emany things that can be tried:
# Take the input as 2 different series

# Apply CNN and then LSTM tend to yield better results
# https://link.springer.com/chapter/10.1007/978-3-030-62463-7_40: Utilization of CNN-LSTM Model in Prediction of Multivariate Time Series for UCG

# Since these are multivariate time series, Transformers approach could be interesting also.
# https://arxiv.org/abs/2010.02803 : A Transformer-based Framework for Multivariate Time Series Representation Learning

# Wavelets/Fourier transform are approaches taken by other groups - as you might have seen during teh DEMO day.

import pandas as pd
import keras
import os
import numpy as np
import matplotlib.pyplot as plt

"""## DATA"""

# input folder where the files lie in
input_dir = os.getcwd()

# load dataset
f_name = os.path.join(input_dir, "out.csv")
dataset = pd.read_csv(f_name)
columns = ["Timestamp","prices","total_volumes"]

# your dataset is too small
d_ts = dataset[columns]
d_ts.head()

# the volume does not have cearly identifiable trend
# prices have a big peak around data 120
dataset["total_volumes"].plot()

# the prices have an ascending trend
# prices have a big peak around data 120
dataset["prices"].plot()

# the prices are slightly correlated to volume
dataset[["prices", "total_volumes"]].corr()

"""## DATA PREPARATION"""

# in order to train a LSTM you must format the data in a certain way:
# Nsamples, Timestep and features
# In the setup decided above ( we take the 29 previous values for volume + the 29 previous values of price)    
# we can not use the volume only, as u saw the correlation between volume and price is rather low

# we create empty lists
# where we are going to store elements of interest
volumes = []
prices = []
targets = []
full_data =[]


# we iterate over the dataset by windows of 30 - this should be parameterised

for idx in range(d_ts.shape[0]-30):
    
    # you cna print each step for better understanding
    # transposing helps when you want to keep windowed data
    transposed = (d_ts.iloc[idx:idx+30,:].T)
    df_volume = pd.DataFrame(transposed.loc[["total_volumes"]])
    
    # comprehension list to rename columns
    df_volume.columns = ["volume_"+ str(i) for i in range(30)]
    # drop last column (the 30th value is in fact the value @ time t)
    # we must drop it because it would be "forward looking" error
    df_volume.drop(df_volume.columns[-1], axis=1, inplace=True)
    
    
    df_price = pd.DataFrame(transposed.loc[["prices"]])
    
    # we have all the values + the target
    # thsi value must be stored in a different variable
    
    df_price.columns = ["price_"+ str(i) for i in range(29)]+["target"]
    
    # the 
    target = df_price[df_price.columns[-1]]
    
    # drop last column (the 30th value is in fact the value @ time t)
    df_price.drop(df_price.columns[-1], inplace=True, axis=1)

    
    # we append to the targets list each value for the target variable
    targets.append(target.values[0])
    
    # input dataframe for volume
    vol_df = df_volume.T.reset_index(drop=True)
    
    # input dataframe for price
    pr_df = df_price.T.reset_index(drop=True)
    
    # final lists where we stored the processed info
    volumes.append(vol_df)
    prices.append(pr_df)
    full_data.append(pd.concat([vol_df,pr_df], axis=1).values)

# data must be casted to float 32 to work with keras
keras_dataset_inputs = np.array(full_data).astype('float32')

# data must be casted to float 32 to work with keras
keras_dataset_targets = np.array(targets).astype('float32')

# we should use a random splitter
# but we are with time series 
# no shuffling
index_of_split = int(keras_dataset_targets.shape[0]*0.8)

# training set and testing set final preparation
training_dataset = keras_dataset_inputs[:index_of_split,:,:]
testing_dataset = keras_dataset_inputs[index_of_split:,:,:]

training_target = np.expand_dims(keras_dataset_targets[:index_of_split], axis=-1)
testing_target = np.expand_dims(keras_dataset_targets[index_of_split:], axis=-1)

###  Shapes respect (nsamples, nsteps, nfeatures)

training_testing_input_shapes = pd.DataFrame([training_dataset.shape,testing_dataset.shape])
training_testing_input_shapes.columns =["samples","steps","features"]           
training_testing_target_shapes = pd.DataFrame([training_target.shape, testing_target.shape])
training_testing_target_shapes.columns =["samples","dim"]

# training vs testing shapes (targets)
training_testing_target_shapes

# training vs testing shapes (inputs)
training_testing_input_shapes

"""## MODEL"""

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout


# this model structure is totally arbitrary
# please check with the litterature
model = Sequential()
model.add(LSTM(units=96, return_sequences=True, input_shape=(training_dataset.shape[1],training_dataset.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=96,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96,return_sequences=True))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.summary()

# usual setup:
# Adam in general converges better
# the loss is totally arbitrary here (u could use : MSE/MAE because it is a regression)
model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.MeanSquaredError())

# actual training
# you can reduce the verbose parameter
history_model=model.fit(training_dataset,
                        training_target,
                        epochs=20,
                        validation_data=(testing_dataset,testing_target),
                        batch_size=1,
                        verbose=1)

# there are many things that are not ok
# you must for example : rescale the data because one dimension is too big compared to the other
# do not do deep learning if you have that few data points

history_model.history['loss']

#you can capture in history : training loss and validation loss 
history_model.history