from flask import Flask

from app import tasks

from app.controllers import btc, eth

from app.tasks import bitcoin, ethereum  # noqa: F401 -> importing tasks


def create_app():
    app = Flask(__name__)

    # register routes
    btc.start(app)
    eth.start(app)

    # start jobs
    tasks.start(app)

    return app
