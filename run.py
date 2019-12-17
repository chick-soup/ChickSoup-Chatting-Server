from flask import Flask

from const import _localRunSetting

from app import create_app
from config.appConfig import localLevelConfig


if __name__ == '__main__':
    app, socketIO = create_app(localLevelConfig)
    socketIO.run(app, **_localRunSetting)