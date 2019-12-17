from const import _productionRunSetting

from app import create_app
from config.appConfig import productionLevelConfig


if __name__ == '__main__':
    app = create_app(productionLevelConfig)
    app.run(**_productionRunSetting)