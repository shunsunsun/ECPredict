from os.path import abspath, dirname, join

_BASEDIR = join(dirname(dirname(abspath(__file__))), 'models')

TRAINED_MODELS = {
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

TEST_MED_ABS_ERRORS = {
    'CN_alvadesc': 5.1397,
    'CN_padel': 6.0640,
    'CP_alvadesc': 4.8851,
    'CP_padel': 8.7707,
    'KV_alvadesc': 0.0725,
    'KV_padel': 0.2153,
    'MON_alvadesc': 2.6142,
    'MON_padel': 12.1012,
    'OS_alvadesc': 2.0652,
    'OS_padel': 6.8286,
    'PP_alvadesc': 3.2287,
    'PP_padel': 3.4133,
    'RON_alvadesc': 2.9913,
    'RON_padel': 9.7657,
    'YSI_alvadesc': 3.3627,
    'YSI_padel': 4.8894
}
