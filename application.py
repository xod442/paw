from flask import Flask


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)

    from main.views import main_app
    app.register_blueprint(main_app)

    from stores.views import stores_app
    app.register_blueprint(stores_app)

    from strains.views import strains_app
    app.register_blueprint(strains_app)

    from auth.views import auth_app
    app.register_blueprint(auth_app)


    return app
