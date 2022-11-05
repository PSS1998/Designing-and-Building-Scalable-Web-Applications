from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def initialize_db(app):
    db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    return db

