from server.models import db 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)

    def set_password(self, password: str) -> None:
        """
        Hashes a plaintext password and stores it securely.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Checks a plaintext password against the stored hash.
        Returns True if matched, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        """
        Returns a safe, serializable dictionary of the user.
        Excludes sensitive fields like password_hash.
        """
        return {
            'id': self.id,
            'username': self.username
        }

    def __repr__(self) -> str:
        return f"<User {self.username}>"
