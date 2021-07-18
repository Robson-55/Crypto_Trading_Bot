#Importing Libraries

import pandas as pd
import keras
import os
import numpy as np
import matplotlib.pyplot as plt

"""## DATA"""

# input folder where the files lie in
input_dir = os.getcwd()

#Load dataset
def load_dataset(file,input_dir):
  f_name = os.path.join(input_dir, file)
  dataset = pd.read_csv(f_name)
  columns = ["Timestamp","prices","total_volumes"]
  d_ts = dataset[columns]
  return d_ts
d_ts=load_dataset("out.csv",input_dir)
d_ts.head()
'''Data Exploration'''
def data_exploration(dataframe):
    print("Some information about the data")
    print(dataframe.head())
    print("Volumes graph")
    dataframe["Volume"].plot()
    print("Prices Graph")
    dataset["prices"].plot()
    print("Correlation between prices and volumes:")
    dataset[["prices", "total_volumes"]].corr()

"""## DATA PREPARATION"""

# For training the LSTM, data must be formatted in a certain way:
# Nsamples, Timestep and features
# In the setup decided above ( we take the 29 previous values for volume + the 29 previous values of price)
# we can not use the volume only, as u saw the correlation between volume and price is rather low

# This function will create windows of a certain length for prices and volumes and store them in lists (price, volume and price-volume lists)

def windows(dataframe, window_length=30):
    # we create empty lists
    # where we are going to store elements of interest

    volumes = []
    prices = []
    targets = []
    full_data = []

    # we iterate over the dataset by windows of window_length(default=30)

    for idx in range(dataframe.shape[0] - window_length):
        # Windowed volume data
        transposed = (dataframe.iloc[idx:idx + window_length, :].T)
        df_volume = pd.DataFrame(transposed.loc[["total_volumes"]])

        # comprehension list to rename columns
        df_volume.columns = ["volume_" + str(i) for i in range(window_length)]
        # drop last column (the 30th value is in fact the value at time t)
        # we must drop it because it would be "forward looking" error
        df_volume.drop(df_volume.columns[-1], axis=1, inplace=True)

        # Windowed price data
        df_price = pd.DataFrame(transposed.loc[["prices"]])

        # we have all the values + the target
        # the target value must be stored in a different variable

        df_price.columns = ["price_" + str(i) for i in range(window_length - 1)] + ["target"]

        # target value
        target = df_price[df_price.columns[-1]]

        # drop last column (the 30th value is in fact the value at time t)
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
        full_data.append(pd.concat([vol_df, pr_df], axis=1).values)

    return volumes, prices, full_data, targets

# Assigning the windows to variables
volumes, prices, full_data, targets = windows(d_ts)

# data must be casted to float 32 to work with keras
def convert_type_keras(full_data, targets):
  keras_dataset_inputs = np.array(full_data).astype('float32')
  keras_dataset_targets = np.array(targets).astype('float32')
  return keras_dataset_inputs, keras_dataset_targets

keras_dataset_inputs,keras_dataset_targets = convert_type_keras(full_data, targets)

# This function will split data to train and test sets, without splitting as the order of the time series is crutial.
def train_test_splitting(keras_dataset_inputs,keras_dataset_targets):
  index_of_split = int(keras_dataset_targets.shape[0]*0.8)
  # training set and testing set final preparation
  training_dataset = keras_dataset_inputs[:index_of_split,:,:]
  testing_dataset = keras_dataset_inputs[index_of_split:,:,:]

  training_target = np.expand_dims(keras_dataset_targets[:index_of_split], axis=-1)
  testing_target = np.expand_dims(keras_dataset_targets[index_of_split:], axis=-1)
  #print(training_dataset.shape)
  #print(testing_dataset) #will output 25 (test set) time windows of lenth 29 days including both prices and volumes
  #print(training_target.shape)
  #print(testing_target)
  return training_dataset, testing_dataset, training_target, testing_target

training_dataset, testing_dataset, training_target, testing_target=train_test_splitting(keras_dataset_inputs,keras_dataset_targets)

###  Shapes must respect (nsamples, nsteps, nfeatures)

#This function stores shapes of training and testing datasets and its targets
def shaping(training_dataset,testing_dataset,training_target,testing_target):
  training_testing_input_shapes = pd.DataFrame([training_dataset.shape,testing_dataset.shape])
  training_testing_input_shapes.columns =["samples","steps","features"]
  training_testing_target_shapes = pd.DataFrame([training_target.shape, testing_target.shape])
  training_testing_target_shapes.columns =["samples","dim"]

  return training_testing_input_shapes,training_testing_target_shapes

training_testing_input_shapes,training_testing_target_shapes=shaping(training_dataset,testing_dataset,training_target,testing_target)
# training vs testing shapes (targets)
training_testing_target_shapes

# training vs testing shapes (inputs)
training_testing_input_shapes

"""## MODEL"""

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout


def lstm_model():
    # Model architecture

    model = Sequential()
    model.add(LSTM(units=96, return_sequences=True, input_shape=(training_dataset.shape[1], training_dataset.shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    # Optimizer and Loss
    model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.MeanSquaredError())

    return model

model=lstm_model()
model.summary()

# This functions trains the model by fitting it to the training and test sets for a certain number of epochs
def train_model(model,epochs=100):
  history_model=model.fit(training_dataset,
                        training_target,
                        epochs=epochs,
                        validation_data=(testing_dataset,testing_target),
                        batch_size=1,
                        verbose=1)
  return history_model

epochs=20
#Assigning the training of the model to a variable, which once called will initialize the training
history_model=train_model(model,epochs)
#Initializing the training:
history_model

#This function will plot both model training and validation lossed during training
def model_metrics(history_model, epochs):
  training_loss=history_model.history["loss"]
  validation_loss=history_model.history["val_loss"]

  epochs=range(1,epochs+1)
  plt.plot(epochs,training_loss, color = 'b', label= 'Training loss')
  plt.plot(epochs,validation_loss, color = 'g', label= 'Validation loss')
  plt.legend()

model_metrics(history_model, epochs)
