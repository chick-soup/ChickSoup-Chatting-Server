from const import _productionRunSetting

from app import create_app
from config.appConfig import productionLevelConfig


if __name__ == '__main__':
    app, socketIO = create_app(productionLevelConfig)
    socketIO.run(app, **_productionRunSetting)