from os.path import abspath, dirname, join

_BASEDIR = join(dirname(dirname(abspath(__file__))), 'models')

TRAINED_MODELS = {
    'CN_alvadesc': join(_BASEDIR, 'cn_database_v2.0.prj'),
    'CN_padel': join(_BASEDIR, 'cn_database_v2.1.prj'),
    'CP_alvadesc': join(_BASEDIR, 'cp_database_v1.0.prj'),
    'CP_padel': join(_BASEDIR, 'cp_database_v1.1.prj'),
    'KV_alvadesc': join(_BASEDIR, 'kv_database_v1.0.prj'),
    'KV_padel': join(_BASEDIR, 'kv_database_v1.1.prj'),
    'MON_alvadesc': join(_BASEDIR, 'mon_database_v1.0.prj'),
    'MON_padel': join(_BASEDIR, 'mon_database_v1.1.prj'),
    'OS_alvadesc': join(_BASEDIR, 's_database_v1.0.prj'),
    'OS_padel': join(_BASEDIR, 's_database_v1.1.prj'),
    'PP_alvadesc': join(_BASEDIR, 'pp_database_v1.0.prj'),
    'PP_padel': join(_BASEDIR, 'pp_database_v1.1.prj'),
    'RON_alvadesc': join(_BASEDIR, 'ron_database_v1.0.prj'),
    'RON_padel': join(_BASEDIR, 'ron_database_v1.1.prj'),
    # 'YSI_alvadesc': join(_BASEDIR, 'ysi_database_v2.0.prj'),
    'YSI_padel': join(_BASEDIR, 'ysi_database_v2.1.prj')
}

TEST_MED_ABS_ERRORS = {
    'CN_alvadesc': 4.7396,
    'CN_padel': 6.0365,
    'CP_alvadesc': 0.2948,
    'CP_padel': 0.5663,
    'KV_alvadesc': 0.0854,
    'KV_padel': 0.2754,
    'MON_alvadesc': 3.6852,
    'MON_padel': 8.9445,
    'OS_alvadesc': 2.1806,
    'OS_padel': 6.7776,
    'PP_alvadesc': 4.0101,
    'PP_padel': 3.7044,
    'RON_alvadesc': 4.2830,
    'RON_padel': 10.0855,
    # 'YSI_alvadesc': 4.8907,
    'YSI_padel': 6.8713
}
