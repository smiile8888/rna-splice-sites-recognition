from keras.layers import Input
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
from keras.models import Model, Sequential
from keras.layers.recurrent import LSTM, GRU
from keras.layers import Bidirectional
from keras.utils import to_categorical
from keras.optimizers import SGD, RMSprop

from sklearn import metrics
import numpy as np
import math

# Constant variables
HIDDEN_1 = 70
HIDDEN_2_3 = 100
HIDDEN_4 = 200
HIDDEN_5 = 250
DENSE_1 = 512
DROPOUT = 0.2

OUTPUT = 2

# Hyperparameters
BATCH_SIZE = 64
START_LR = 0.05
STEPS_PER_LR_DECAY = 5
LR_DECAY = 0.5
EPOCH = 30


def stepDecay(epoch):
    """
    Callback function for setting up learning rate decay
    :param epoch: number of epoch showing when the learning rate will be decayed
    :return: an updated learning rate
    """
    lr = START_LR * math.pow(LR_DECAY, math.floor((1 + epoch) / STEPS_PER_LR_DECAY))
    return lr


def Vmodel_1(sequenceLength):
    inputs = Input(shape=(sequenceLength, 4, 1))

    conv1 = Conv2D(HIDDEN_1, (3, 4), activation='relu')(inputs)
    dropout1 = Dropout(DROPOUT)(conv1)

    conv2 = Conv2D(HIDDEN_2_3, (3, 1), activation='relu')(dropout1)
    dropout2 = Dropout(DROPOUT)(conv2)

    conv3 = Conv2D(HIDDEN_2_3, (3, 1), activation='relu')(dropout2)
    maxPool1 = MaxPooling2D(pool_size=(2, 1))(conv3)
    dropout3 = Dropout(DROPOUT)(maxPool1)

    conv4 = Conv2D(HIDDEN_4, (3, 1), activation='relu')(dropout3)
    maxPool2 = MaxPooling2D(pool_size=(2, 1))(conv4)
    dropout4 = Dropout(DROPOUT)(maxPool2)

    flatten1 = Flatten()(dropout4)

    dense1 = Dense(DENSE_1, activation='relu')(flatten1)
    dropout5 = Dropout(DROPOUT)(dense1)

    outputs = Dense(2, activation='softmax')(dropout5)

    model = Model(inputs=inputs, outputs=outputs)

    return model


def Vmodel_2(sequenceLength):
    inputs = Input(shape=(sequenceLength, 4, 1))

    conv1 = Conv2D(HIDDEN_1, (5, 4), activation='relu')(inputs)
    dropout1 = Dropout(DROPOUT)(conv1)

    conv2 = Conv2D(HIDDEN_2_3, (3, 1), activation='relu')(dropout1)
    dropout2 = Dropout(DROPOUT)(conv2)

    flatten1 = Flatten()(dropout2)

    dense1 = Dense(DENSE_1, activation='relu')(flatten1)
    dropout3 = Dropout(DROPOUT)(dense1)

    outputs = Dense(2, activation='softmax')(dropout3)

    model = Model(inputs=inputs, outputs=outputs)

    return model


def Vmodel_3(sequenceLength):
    inputs = Input(shape=(sequenceLength, 4, 1))

    dense1 = Dense(128, activation='relu')(inputs)
    flatten1 = Flatten()(dense1)

    outputs = Dense(2, activation='softmax')(flatten1)

    model = Model(inputs=inputs, outputs=outputs)

    return model


def SpliceRover(sequenceLength):
    # SpliceRover Model
    inputs = Input(shape=(sequenceLength, 4, 1))

    conv1 = Conv2D(70, (9, 4), activation='relu')(inputs)
    dropout1 = Dropout(0.2)(conv1)

    conv2 = Conv2D(100, (7, 1), activation='relu')(dropout1)
    maxPool1 = MaxPooling2D(pool_size=(2, 1))(conv2)
    dropout2 = Dropout(0.2)(maxPool1)

    conv3 = Conv2D(150, (7, 1), activation='relu')(dropout2)
    maxPool2 = MaxPooling2D(pool_size=(2, 1))(conv3)
    dropout3 = Dropout(0.2)(maxPool2)

    dense1 = Dense(512, activation='relu')(dropout3)
    dropout4 = Dropout(0.2)(dense1)

    flatten1 = Flatten()(dropout4)

    outputs = Dense(2, activation='softmax')(flatten1)

    model = Model(inputs=inputs, outputs=outputs)

    return model


def BLSTM(sequenceLength):
    model = Sequential()
    lstm = LSTM(input_dim=320, output_dim=320, return_sequences=True)
    blstm = Bidirectional(lstm)

    model.add(Convolution1D(input_dim=4,
                            input_length=sequenceLength,
                            nb_filter=320,
                            filter_length=26,
                            border_mode="valid",
                            activation="relu",
                            subsample_length=1))
    model.add(MaxPooling1D(pool_length=13, stride=13))

    model.add(Dropout(0.2))

    model.add(blstm)

    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(input_dim=75 * 640, output_dim=925))
    model.add(Activation("relu"))

    model.add(Dense(input_dim=925, output_dim=2))
    model.add(Activation("softmax"))

    return model