from math import sqrt

from ecpredict.utils.loc_errors import TEST_MED_ABS_ERRORS
from ecpredict.utils.project import get_prj


def _linear_blend_ave(values: list, proportions: tuple) -> float:

    weighted_ave = 0
    for idx, proportion in enumerate(proportions):
        weighted_ave += (proportion * values[idx])
    return weighted_ave


def _linear_blend_err(prop_err: float, proportions: tuple,
                      omit: list) -> float:

    squared_err = 0
    for idx, proportion in enumerate(proportions):
        if omit[idx] is True:
            continue
        else:
            squared_err += (proportion**2 * prop_err**2)
    return sqrt(squared_err)


def cetane_number_blend(smiles_and_vals: tuple, proportions: tuple,
                        backend: str = 'padel') -> tuple:

    trained_prj = get_prj('CN', backend)
    cn_values = []
    omit = []
    for item in smiles_and_vals:
        if type(item) is str:
            cn_values.append(trained_prj.use([item], backend)[0])
            omit.append(False)
        else:
            cn_values.append(item)
            omit.append(True)
    return (_linear_blend_ave(cn_values, proportions),
            _linear_blend_err(TEST_MED_ABS_ERRORS['CN_{}'.format(backend)],
                              proportions, omit))


def yield_sooting_index_blend(smiles_and_vals: tuple, proportions: tuple,
                              backend: str = 'padel') -> tuple:

    trained_prj = get_prj('YSI', backend)
    ysi_values = []
    omit = []
    for item in smiles_and_vals:
        if type(item) is str:
            ysi_values.append(trained_prj.use([item], backend)[0])
            omit.append(False)
        else:
            ysi_values.append(item)
            omit.append(True)
    return (_linear_blend_ave(ysi_values, proportions),
            _linear_blend_err(TEST_MED_ABS_ERRORS['YSI_{}'.format(backend)],
                              proportions, omit))
