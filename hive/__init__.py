from eve import Eve

from hive.main.hive_mongo import HiveMongo
from hive.util.auth import HiveTokenAuth
from hive import main

DEFAULT_APP_NAME = 'Hive Node'

configs = {
    'development': "settings_dev.py",
    'testing': "settings_test.py",
    'production': "settings.py",
    'default': "settings_dev.py"
}


def create_app(config='default'):
    app = Eve(auth=HiveTokenAuth, settings=configs[config])
    main.init_app(app)
    return app

