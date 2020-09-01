from flask_oidc import OpenIDConnect
from flask_sqlalchemy import SQLAlchemy

login = OpenIDConnect()

db = SQLAlchemy()
