#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/predict.py
# v.0.1.0
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains function for predicting properties using pre-trained .prj files
# built using ECNet
#

# Stdlib imports
from os.path import abspath, dirname, join

# ECPredict imports
from ecpredict.utils.project import TrainedProject

_BASEDIR = join(dirname(abspath(__file__)), 'models')

_TRAINED_MODELS = {
    'CN_alvadesc': join(_BASEDIR, 'cn_model_v2.0.prj'),
    'CN_padel': join(_BASEDIR, 'cn_model_v2.1.prj'),
    'CP_alvadesc': join(_BASEDIR, 'cp_model_v1.0.prj'),
    'CP_padel': join(_BASEDIR, 'cp_model_v1.1.prj'),
    'KV_alvadesc': join(_BASEDIR, 'kv_model_v1.0.prj'),
    'KV_padel': join(_BASEDIR, 'kv_model_v1.1.prj'),
    'MON_alvadesc': join(_BASEDIR, 'mon_model_v1.0.prj'),
    'MON_padel': join(_BASEDIR, 'mon_model_v1.1.prj'),
    'OS_alvadesc': join(_BASEDIR, 'os_model_v1.0.prj'),
    'OS_padel': join(_BASEDIR, 'os_model_v1.1.prj'),
    'PP_alvadesc': join(_BASEDIR, 'pp_model_v1.0.prj'),
    'PP_padel': join(_BASEDIR, 'pp_model_v1.1.prj'),
    'RON_alvadesc': join(_BASEDIR, 'ron_model_v1.0.prj'),
    'RON_padel': join(_BASEDIR, 'ron_model_v1.1.prj'),
    'YSI_alvadesc': join(_BASEDIR, 'ysi_model_v2.0.prj'),
    'YSI_padel': join(_BASEDIR, 'ysi_model_v2.1.prj')
}

_TEST_MED_ABS_ERRORS = {
    'CN_alvadesc': 6.6711,
    'CN_padel': 6.3840,
    'CP_alvadesc': 0.6421,
    'CP_padel': 1.2351,
    'KV_alvadesc': 0.0618,
    'KV_padel': 0.1991,
    'OS_alvadesc': 2.0616,
    'PP_alvadesc': 3.9422,
    'PP_padel': 9.6152,
    'RON_alvadesc': 3.8861,
    'YSI_alvadesc': 3.6471,
    'YSI_padel': 4.6917
}


def _get_prj(prop: str, backend: str) -> TrainedProject:

    to_use = '{}_{}'.format(prop, backend)
    available_models = list(_TRAINED_MODELS.keys())
    if to_use not in available_models:
        raise IndexError('Model for `{}` trained with `{}` descriptors not '
                         'found in available models: {}'.format(
                             prop, backend, available_models
                         ))
    return TrainedProject(_TRAINED_MODELS[to_use])


def cetane_number(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = _get_prj('CN', backend)
    return (trained_prj.use(smiles, backend),
            _TEST_MED_ABS_ERRORS['CN_{}'.format(backend)])


def cloud_point(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = _get_prj('CP', backend)
    return (trained_prj.use(smiles, backend),
            _TEST_MED_ABS_ERRORS['CP_{}'.format(backend)])


def kinematic_viscosity(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = _get_prj('KV', backend)
    return (trained_prj.use(smiles, backend),
            _TEST_MED_ABS_ERRORS['KV_{}'.format(backend)])


def pour_point(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = _get_prj('PP', backend)
    return (trained_prj.use(smiles, backend),
            _TEST_MED_ABS_ERRORS['PP_{}'.format(backend)])


def yield_sooting_index(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = _get_prj('YSI', backend)
    return (trained_prj.use(smiles, backend),
            _TEST_MED_ABS_ERRORS['YSI_{}'.format(backend)])
