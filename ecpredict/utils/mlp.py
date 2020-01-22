#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/utils/mlp.py
# v.0.1.0
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains the "MultilayerPerceptron" (feed-forward neural network) class
#

# Stdlib imports
from os import environ

# 3rd party imports
from numpy import array_equiv
from tensorflow.keras.models import load_model

environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class MultilayerPerceptron:

    def __init__(self, filename: str):
        ''' MultilayerPerceptron: Feed-forward neural network; uses a
        pre-trained .h5 sequential model to predict values

        Args:
            filename (str): filename/path for the model
        '''

        self._model = load_model(filename, compile=False)

    def use(self, x: array) -> array:
        ''' use: uses the model to predict values for supplied data

        Args:
            x (np.array): input data to predict for

        Returns:
            np.array: predicted values
        '''

        return self._model.predict(x)
