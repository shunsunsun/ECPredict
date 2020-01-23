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
from re import compile, IGNORECASE, sub
from tempfile import TemporaryDirectory
from zipfile import ZipFile

# 3rd party imports
from alvadescpy import smiles_to_descriptors
from numpy import asarray, mean
from padelpy import from_smiles

# ECPredict imports
from ecpredict.utils.mlp import MultilayerPerceptron

MODEL_RE = compile(r'^.*\.h5$', IGNORECASE)


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

        self._inp_names = None
        self._models = []

        with ZipFile(filename, 'r') as zf:
            prj_zip = zf.namelist()
            with TemporaryDirectory() as tmpdirname:
                zf.extractall(tmpdirname)
                prj_dirname = join(tmpdirname, basename(
                    filename.replace('.prj', '')
                ))
                with open(join(prj_dirname, 'inp.txt'), 'r') as txt_file:
                    self._inp_names = txt_file.readlines()
                txt_file.close()
                for idx, line in enumerate(self._inp_names):
                    self._inp_names[idx] = sub(r'\n$', '', line)
                for root, _, files in walk(prj_dirname):
                    for f in files:
                        if MODEL_RE.match(f) is not None:
                            _model = MultilayerPerceptron(join(root, f))
                            self._models.append(_model)

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
        preds = mean([model.use(asarray(
            [[float(mol[name]) for name in self._inp_names]
             for mol in mols]
        )) for model in self._models], axis=0)
        return [p[0] for p in preds]
