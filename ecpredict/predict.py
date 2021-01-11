#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/predict.py
# v.0.1.1
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains function for predicting properties using pre-trained .prj files
# built using ECNet
#

# ECPredict imports
from ecpredict.utils.loc_errors import TEST_MED_ABS_ERRORS
from ecpredict.utils.project import get_prj


def cetane_number(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('CN', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['CN_{}'.format(backend)])


def cloud_point(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('CP', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['CP_{}'.format(backend)])


def kinematic_viscosity(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('KV', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['KV_{}'.format(backend)])


def motor_octane_number(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('MON', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['MON_{}'.format(backend)])


def octane_sensitivity(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('OS', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['OS_{}'.format(backend)])


def pour_point(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('PP', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['PP_{}'.format(backend)])


def research_octane_number(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('RON', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['RON_{}'.format(backend)])


def yield_sooting_index(smiles: list, backend: str = 'padel') -> tuple:

    # Temp. force to PaDEL
    backend = 'padel'
    trained_prj = get_prj('YSI', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['YSI_{}'.format(backend)])
