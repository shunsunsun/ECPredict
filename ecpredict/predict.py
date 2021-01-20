#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/predict.py
# v.0.1.3
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains function for predicting properties using pre-trained .prj files
# built using ECNet
#

# ECPredict imports
from ecpredict.utils.loc_errors import TEST_MED_ABS_ERRORS
from ecpredict.utils.project import get_prj
from ecpredict.utils.equations import _density, _dulong

# 3rd party imports
from padelpy import from_smiles


def cetane_number(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('CN', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['CN_{}'.format(backend)])


def cloud_point(smiles: list, backend: str = 'padel') -> tuple:

    trained_prj = get_prj('CP', backend)
    return (trained_prj.use(smiles, backend),
            TEST_MED_ABS_ERRORS['CP_{}'.format(backend)])


def lower_heating_value(smiles: list) -> tuple:

    desc = from_smiles(smiles)
    counts = [[
        int(d['nC']),
        int(d['nH']),
        int(d['nO']),
        int(d['nS'])
    ] for d in desc]
    totals = [sum(c) for c in counts]
    props = [[c / totals[i] for c in cnt] for i, cnt in enumerate(counts)]
    res_dulong = []
    for p in props:
        res_dulong.append(_dulong(p[0], p[1], p[2], p[3]))
    densities = []
    for c in counts:
        densities.append(_density(c[0], c[1], c[2], c[3]))
    lhv = []
    for idx, d in enumerate(densities):
        lhv.append(res_dulong[idx] * d)
    errors = []
    for l in lhv:
        # error assumed at 3.8%
        errors.append(0.038 * l)
    return (lhv, errors)


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
