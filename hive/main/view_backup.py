from flask import Blueprint

from hive.main.hive_backup import HiveBackup

h_backup = HiveBackup()
hive_backup = Blueprint('hive_backup', __name__)


def init_app(app, mode):
    h_backup.init_app(app, mode)
    app.register_blueprint(hive_backup)


@hive_backup.route('/api/v1/backup/save/to/google_drive', methods=['POST'])
def save_to_google_drive():
    return h_backup.save_to_google_drive()


@hive_backup.route('/api/v1/backup/restore/from/google_drive', methods=['POST'])
def restore_from_google_drive():
    return h_backup.restore_from_google_drive()


@hive_backup.route('/api/v1/backup/state', methods=['GET'])
def get_sync_google_drive_state():
    return h_backup.get_sync_google_drive_state()