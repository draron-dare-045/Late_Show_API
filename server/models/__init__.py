from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Import all models to register them and resolve relationships
from .guest import Guest
from .episode import Episode
from .appearance import Appearance

__all__ = ["db", "migrate"]