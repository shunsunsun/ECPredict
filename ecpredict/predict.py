#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/predict.py
# v.0.1.2
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains function for predicting properties using pre-trained .prj files
# built using ECNet
#

# ECPredict imports
from ecpredict.utils.loc_errors import TEST_MED_ABS_ERRORS
from ecpredict.utils.project import get_prj

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


def heat_of_combustion(smiles: list) -> tuple:

    desc = from_smiles(smiles)
    counts = [[
        int(d['nC']),
        int(d['nH']),
        int(d['nS']),
        int(d['nO']),
        int(d['nN'])
    ] for d in desc]
    totals = [sum(c) for c in counts]
    props = [[c / totals[i] for c in cnt] for i, cnt in enumerate(counts)]
    res_dulong = []
    res_boie = []
    res_lloyd_davenport = []
    for p in props:
        res_dulong.append(
            -0.3390 * p[0] - 1.433 * p[1] - 0.094 * p[2] + 0.179 * p[3]
        )
        res_boie.append(
            -0.3578 * p[0] - 1.1357 * p[1] + 0.0845 * p[3] - 0.0594 * p[4]\
                - 0.1119 * p[2]
        )
        res_lloyd_davenport.append(
            -0.35777 * p[0] - 0.91758 * p[1] + 0.08451 * p[3] - 0.05938 * p[4]\
                - 0.11187 * p[2]
        )
    err_dulong = [abs(0.036 * r) for r in res_dulong]
    err_boie = [abs(0.0094 * r) for r in res_boie]
    err_lloyd_davenport = [abs(0.005 * r) for r in res_lloyd_davenport]
    return (
        [(res_dulong[i] + res_boie[i] + res_lloyd_davenport[i]) / 3
         for i in range(len(res_dulong))],
        [(err_dulong[i] + err_boie[i] + err_lloyd_davenport[i]) / 3
         for i in range(len(err_dulong))]
    )


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
