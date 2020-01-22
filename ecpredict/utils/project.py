#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/utils/project.py
# v.0.1.0
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains functions for predicting data using pre-existing .prj files
#

# Stdlib imports
from os import walk
from os.path import basename, join
from pickle import dump as pdump, load as pload
from re import compile, IGNORECASE
from tempfile import TemporaryDirectory
from zipfile import ZipFile

# 3rd party imports
from alvadescpy import smiles_to_descriptors
from numpy import asarray, mean
from padelpy import from_smiles
from yaml import load, FullLoader

# ECPredict imports
from ecpredict.utils.mlp import MultilayerPerceptron

from ecnet.utils.server_utils import open_config, open_df

CONFIG_RE = compile(r'^.*\.yml$', IGNORECASE)
MODEL_RE = compile(r'^.*\.h5$', IGNORECASE)


def open_config(filename: str) -> dict:
    '''Returns contents of YML model configuration file

    Args:
        filename (str): path to YML configuration file

    Returns:
        dict: variable names and values
    '''

    with open(filename, 'r') as cf_file:
        return load(cf_file, FullLoader)


def open_df(filename: str) -> 'DataFrame':
    '''Opens pickled DataFrame object

    Args:
        filename (str): path to pickled file

    Returns:
        DataFrame: opened DataFrame
    '''

    with open(filename, 'rb') as data_file:
        return pload(data_file)


class TrainedProject:

    def __init__(self, filename: str):
        ''' TrainedProject: loads a trained ECNet project, including last-used
        DataFrame, configuration .yml file, and all trained models

        Args:
            filename (str): name/path of the trained .prj file
        '''

        self._df = None
        self._config = None
        self._models = []

        with ZipFile(filename, 'r') as zf:
            prj_zip = zf.namelist()
            with TemporaryDirectory() as tmpdirname:
                zf.extractall(tmpdirname)
                prj_dirname = join(tmpdirname, basename(
                    filename.replace('.prj', '')
                ))
                self._df = open_df(join(prj_dirname, 'data.d'))
                for root, _, files in walk(prj_dirname):
                    for f in files:
                        if MODEL_RE.match(f) is not None:
                            _model = MultilayerPerceptron(join(root, f))
                            _model.load()
                            self._models.append(_model)
                        elif CONFIG_RE.match(f) is not None:
                            self._config = open_config(join(root, f))

    def use(self, smiles: list, backend: str = 'padel'):
        ''' use: uses the trained project to predict values for supplied
        molecules

        Args:
            smiles (list): list of SMILES strings to predict for
            backend (str): backend software to use for QSPR generation; `padel`
                or `alvadesc`; default = `padel`; alvadesc requries valid
                license

        Returns:
            numpy.array: predicted values
        '''

        if backend == 'alvadesc':
            mols = [smiles_to_descriptors(s) for s in smiles]
            for mol in mols:
                for key in list(mol.keys()):
                    if mol[key] == 'na':
                        mol[key] = 0
        elif backend == 'padel':
            mols = [from_smiles(s) for s in smiles]
        else:
            raise ValueError('Unknown backend software: {}'.format(backend))
        return mean([model.use(asarray(
            [[float(mol[name]) for name in self._df._input_names]
             for mol in mols]
        )) for model in self._models], axis=0)
