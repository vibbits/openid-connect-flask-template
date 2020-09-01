from flask import Flask

def register_extensions(app: Flask) -> None:
    from application.extensions import login, db

    login.init_app(app)
    db.init_app(app)

def register_blueprints(app: Flask) -> None:
    from application.webapp import main

    app.register_blueprint(main)

def create_app() -> Flask:
    """ Top-level app factory. """
    flaskapp = Flask(__name__)
    flaskapp.config.update({
        "TESTING": True,
        "DEBUG": True,
        'SECRET_KEY': "fake",
        "OIDC_SCOPES": ["openid"],
        "OIDC_CLIENT_SECRETS": "client_secrets.json",
        "OIDC_ID_TOKEN_COOKIE_SECURE": False,
        "OIDC_REQUIRE_VERIFIED_EMAIL": False
    })
        

    register_extensions(flaskapp)
    register_blueprints(flaskapp)

    return flaskapp

server = create_app()
