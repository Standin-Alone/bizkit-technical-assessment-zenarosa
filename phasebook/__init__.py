from flask import Flask

from . import match, search


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    app.register_blueprint(match.bp)
    app.register_blueprint(search.bp)
    app.config["JSON_SORT_KEYS"] = False
    return app
