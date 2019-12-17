from flask import Flask


def create_app(*config_cls) -> Flask:
    flask = Flask(__name__)

    for config in config_cls:
        flask.config.from_object(config)

    return flask