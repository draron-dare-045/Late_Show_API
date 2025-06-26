from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


from .guest import Guest
from .episode import Episode
from .appearance import Appearance

__all__ = ["db", "migrate"]
