#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ecpredict/utils/equations.py
# v.0.1.4
# Developed in 2020 by Travis Kessler <travis.j.kessler@gmail.com>
#
# Contains various equations for formulae, conversions
#

from math import sqrt


def _celsius_to_rankine(temp: float) -> float:
    ''' Converts temperature in celsius to temperature in rankine

    Args:
        temp (float): supplied temperature, in celsius

    Returns:
        float: temperature in rankine
    '''

    return (9 / 5) * temp + 491.67


def _density(c_c: int, c_h: int, c_o: int, c_s: int) -> float:
    ''' Calculates the density, or gram molecular weight (in kg/l)

    Args:
        c_c (int): number of carbon atoms present in the compound
        c_h (int): number of hydrogen atoms present in the compound
        c_o (int): number of oxygenatoms present in the compound
        c_s (int): number of sulfur atoms present in the compound

    Returns:
        float: density of the compound,  in kg/l
    '''

    return (12.011 * c_c + 1.008 * c_h + 15.999 * c_o + 32.06 * c_s) / 1000


def _dulong(p_c: float, p_h: float, p_o: float, p_s: float) -> float:
    ''' https://doi.org/10.1016/j.fuproc.2016.06.040

    Args:
        p_c (float): proportion of carbon atoms in compound
        p_h (float): proportion of hydrogen atoms in compound
        p_o (float): proportion of oxygen atoms in compound
        p_s (float): proportion of sulfur atoms in compound

    Returns:
        float: lower heating value, in kJ/g
    '''

    return 33.8 * p_c + 122.3 * (p_h - p_o / 8) + 9.4 * p_s


def _linear_blend_ave(values: list, proportions: tuple) -> float:
    ''' Calculates the linear combination of multiple values given discrete
    proportions for each value

    Args:
        values (list): list of values to form linear average
        proportions (tuple): proportions of each value in `values`; should sum
            to 1; len(proportions) == len(values)

    Returns:
        float: weighted linear average
    '''

    weighted_ave = 0
    for idx, proportion in enumerate(proportions):
        weighted_ave += (proportion * values[idx])
    return weighted_ave


def _linear_blend_err(prop_err: float, proportions: tuple,
                      omit: list) -> float:
    ''' Calculates the linear combination of an error given multiple components
    with discrete proportions

    Args:
        prop_err (float): supplied error
        proportions (tuple): proportions of each component
        omit (list): list of Boolean values, if True, do not use to calculate

    Returns:
        float: resulting multi-component error
    '''

    squared_err = 0
    for idx, proportion in enumerate(proportions):
        if omit[idx] is True:
            continue
        else:
            squared_err += (proportion**2 * prop_err**2)
    return sqrt(squared_err)


def _linear_blend_err_multi(errs: list, proportions: tuple,
                            omit: list) -> float:
    ''' Calculates the linear combination of multiple errors given multiple
    components with discrete proportions

    Args:
        errs (list): list of errors
        proportions (tuple): weighted proportion of each error
        omit (list): list of Boolean values, if True, do not use to calculate

    Returns:
        float: resulting multi-component error
    '''

    squared_err = 0
    for idx, proportion in enumerate(proportions):
        if omit[idx] is True:
            continue
        else:
            squared_err += (proportion**2 * errs[idx]**2)
    return sqrt(squared_err)


def _rankine_to_celsius(temp: float) -> float:
    ''' Converts temperature in rankine to temperature in celsius

    Args:
        temp (float): temperature in rankine

    Returns:
        float: temperature in celsius
    '''

    return (temp - 491.67) * (1 / (9 / 5))
